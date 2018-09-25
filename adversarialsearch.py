from adversarialsearchproblem import AdversarialSearchProblem
from gamedag import GameDAG, DAGState


def minimax(asp):

	"""
	Implement the minimax algorithm on ASPs
	assuming that the given game is both 2-player and constant-sum

	Input: asp - an AsversarialSearchProblem
	Output: an action
	"""

	start = asp.get_start_state()
	player = start.player_to_move()

	move = minimax_help(asp, start)
	return move


def minimax_help(asp, node):
	start = asp.get_start_state()
	if asp.is_terminal_state(node):
		result = asp.evaluate_state(node)
		return result

	next_player = node.player_to_move()
	value = float('-inf')
	actions = asp.get_available_actions(node)
	for a in actions:
		child = asp.transition(node, a)
		nodes = minimax_help(asp, child)
		if (nodes[next_player] > value):
			value = nodes[next_player]
			best_node = nodes
			prev_move = a
	if (node == start):
		return prev_move
	else:
		return best_node


def alpha_beta(asp):

	start = asp.get_start_state()
	player = start.player_to_move()
	a = float('-inf')
	b = float('inf')

	move = alpha_beta_helper(asp, start, a, b, player)
	return move

def alpha_beta_helper(asp, node, a, b, player):
	start = asp.get_start_state()
	if asp.is_terminal_state(node):
		result = asp.evaluate_state(node)
		return result[player]

	next_player = node.player_to_move()
	if (next_player == player):
		for action in asp.get_available_actions(node):
			child = asp.transition(node, action)
			value = alpha_beta_helper(asp, child, a, b, player)
			if value > a :
				a = value
				prev_move = action
			if a >= b :
				break
		if (node == start):
			return prev_move
		return a

	if (next_player != player):
		for action in asp.get_available_actions(node):
			child = asp.transition(node, action)
			value = alpha_beta_helper(asp, child, a, b, player)
			if value < b :
				b = value
				prev_move = action
			if a >= b:
				break
		if (node == start):
			return prev_move
		return b



def alpha_beta_cutoff(asp, cutoff_ply, eval_func):

	"""
	Alpha-beta with cutoff
	"""

	start = asp.get_start_state()
	player = start.player_to_move()
	a = float('-inf')
	b = float('inf')

	move = cutoff_helper(asp, start, cutoff_ply, a, b, player, eval_func)
	return move

def cutoff_helper(asp, node, cutoff_ply, a, b, player, eval_func):
	start = asp.get_start_state()
	if asp.is_terminal_state(node):
		result = asp.evaluate_state(node)
		return result[player]

	if (cutoff_ply == 0):
		result = eval_func(node)
		return result

	next_player = node.player_to_move()
	if (next_player == player):
		for action in asp.get_available_actions(node):
			child = asp.transition(node, action)
			value = cutoff_helper(asp, child, cutoff_ply-1, a, b, player, eval_func)
			if value > a :
				a = value
				prev_move = action
			if a >= b :
				break
		if (node == start):
			return prev_move
		return a
	
	if (next_player != player):
		for action in asp.get_available_actions(node):
			child = asp.transition(node, action)
			value = cutoff_helper(asp, child, cutoff_ply-1, a, b, player,eval_func)
			if value < b :
				b = value
				prev_move = action
			if a >= b:
				break
		if (node == start):
			return prev_move
		return b


def general_minimax(asp):

	"""
	Implement the minimax algorithm on ASPs
	assuming that the given game is both 2-player and constant-sum

	Input: asp - an AsversarialSearchProblem
	Output: an action
	"""

	start = asp.get_start_state()
	player = start.player_to_move()

	move = general_minimax_help(asp, start, player)
	return move


def general_minimax_help(asp, node, player):
	start = asp.get_start_state()
	if asp.is_terminal_state(node):
		result = asp.evaluate_state(node)
		return result[player]

	next_player = node.player_to_move()
	if (next_player == player):
		value = float('-inf')
		actions = asp.get_available_actions(node)
		for a in actions:
			child = asp.transition(node, a)
			v = general_minimax_help(asp, child, player)
			if (v > value) :
				value = v
				prev_move = a
		if (node == start):
			return prev_move
		return value

	else :
		value = float('inf')
		actions = asp.get_available_actions(node)
		for a in actions:
			child = asp.transition(node, a)
			v = general_minimax_help(asp, child, player)
			if (v < value) :
				value = v
				prev_move = a
		if (node == start):
			return prev_move
		return value





