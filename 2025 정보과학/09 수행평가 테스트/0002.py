
import math
import random

win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def check_winner(board):
	for a,b,c in win:
		s = board[a] + board[b] + board[c]
		if s == 3:
			return 1
		if s == -3:
			return -1
	if 0 not in board:
		return 0
	return None

def moves(board):
	return [i for i, v in enumerate(board) if v == 0]

class TicTacToe:
	def __init__(self, board=None, current_player=1):
		self.board = [0]*9 if board is None else board
		self.current_player = current_player

	def moves(self):
		return moves(self.board)

	def play(self, move):
		if self.board[move] != 0:
			raise ValueError("잘못된 수입니다.")
		self.board[move] = self.current_player
		self.current_player = -self.current_player

	def result(self):
		return check_winner(self.board)

def immediate(board, player):
	for m in moves(board):
		b2 = board.copy()
		b2[m] = player
		if check_winner(b2) == player:
			return m
	return None

def heuristic(board, player):
	m = immediate(board, player)
	if m is not None:
		return m
	opp = -player
	m = immediate(board, opp)
	if m is not None:
		return m
	if board[4] == 0:
		return 4
	corners = [i for i in [0,2,6,8] if board[i] == 0]
	if corners:
		return random.choice(corners)
	sides = [i for i in [1,3,5,7] if board[i] == 0]
	if sides:
		return random.choice(sides)
	return random.choice(moves(board))

class Node:
	def __init__(self, state, parent=None, move=None):
		self.parent = parent
		self.move = move
		self.player_just_moved = -state.current_player
		self.untried_moves = state.moves()
		self.children = {}
		self.wins = 0.0
		self.visits = 0

	def uct_select_child(self, c=1.414):
		return max(
			self.children.values(),
			key=lambda ch: (ch.wins / ch.visits) + c * math.sqrt(math.log(self.visits + 1.0) / ch.visits)
		)

	def add_child(self, move, state_after_move):
		child = Node(state_after_move, parent=self, move=move)
		if move in self.untried_moves:
			self.untried_moves.remove(move)
		self.children[move] = child
		return child

	def update(self, terminal_result):
		self.visits += 1
		if terminal_result == 0:
			self.wins += 0.5
		elif terminal_result == self.player_just_moved:
			self.wins += 1.0

def mcts_search(root_state, itermax=5000, c=1.414, use_heuristic_rollout=True):
	root = Node(root_state)

	for _ in range(itermax):
		node = root
		state = TicTacToe(root_state.board.copy(), root_state.current_player)

		# Selection
		while not node.untried_moves and node.children:
			node = node.uct_select_child(c)
			state.play(node.move)

		# Expansion
		if node.untried_moves:
			move = random.choice(node.untried_moves)
			state.play(move)
			node = node.add_child(move, state)

		# Simulation
		result = state.result()
		while result is None:
			if use_heuristic_rollout:
				mv = heuristic(state.board, state.current_player)
			else:
				mv = random.choice(state.moves())
			state.play(mv)
			result = state.result()

		# Backpropagation
		while node is not None:
			node.update(result)
			node = node.parent

	best_move = max(root.children.items(), key=lambda kv: kv[1].visits)[0]
	return best_move

class MCTS:
	def __init__(self, itermax=8000, c=1.414, use_heuristic_rollout=True):
		self.itermax = itermax
		self.c = c
		self.use_heuristic_rollout = use_heuristic_rollout

	def choose(self, game):
		m = immediate(game.board, game.current_player)
		if m is not None:
			return m
		m = immediate(game.board, -game.current_player)
		if m is not None:
			return m
		return mcts_search(game, self.itermax, self.c, self.use_heuristic_rollout)

SYMBOL = {1: 'X', -1: 'O', 0: ' '}

def printing(board):
	cells = [SYMBOL[v] if v != 0 else str(i+1) for i, v in enumerate(board)]
	lines = [
		f" {cells[0]} | {cells[1]} | {cells[2]} ",
		"---+---+---",
		f" {cells[3]} | {cells[4]} | {cells[5]} ",
		"---+---+---",
		f" {cells[6]} | {cells[7]} | {cells[8]} ",
	]
	print("\n".join(lines))

def human_move(game):
	while True:
		try:
			mv = int(input("당신의 수(1~9): ")) - 1
			if mv in game.moves():
				return mv
		except Exception:
			pass
		print("잘못된 입력입니다. 다시 시도하세요.")

human_is_x = True
ai_iters = 8000
game = TicTacToe(current_player=1)
ai = MCTS(itermax=ai_iters)

print("자리 번호:")
printing([0]*9)
print()

while True:
	printing(game.board)
	res = game.result()
	if res is not None:
		if res == 1:
			print("X 승!")
		elif res == -1:
			print("O 승!")
		else:
			print("무승부!")
		break

	if (game.current_player == 1 and human_is_x) or (game.current_player == -1 and not human_is_x):
		mv = human_move(game)
	else:
		mv = ai.choose(game)
		print(f"AI 수: {mv+1}")
	game.play(mv)
