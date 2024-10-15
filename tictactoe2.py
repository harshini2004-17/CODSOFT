import numpy as np

# Constants for the game
EMPTY = 0
PLAYER_X = 1
PLAYER_O = -1

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = PLAYER_X

    def print_board(self):
        for row in self.board:
            print(" | ".join(['X' if cell == PLAYER_X else 'O' if cell == PLAYER_O else ' ' for cell in row]))
            print("-" * 9)

    def check_winner(self):
        # Check rows, columns and diagonals for a winner
        for i in range(3):
            if abs(sum(self.board[i])) == 3:  # Check rows
                return self.board[i][0]
            if abs(sum(self.board[:, i])) == 3:  # Check columns
                return self.board[0][i]

        if abs(sum(self.board.diagonal())) == 3:  # Check main diagonal
            return self.board[0][0]
        if abs(sum(np.fliplr(self.board).diagonal())) == 3:  # Check anti-diagonal
            return self.board[0][2]

        if np.all(self.board != 0):  # Check for a tie
            return 0  # Tie

        return None  # Game still ongoing

    def make_move(self, row, col):
        if self.board[row, col] == EMPTY:
            self.board[row, col] = self.current_player
            self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X

    def minimax(self, depth, is_maximizing):
        winner = self.check_winner()
        if winner == PLAYER_O:
            return 1  # AI (O) wins
        elif winner == PLAYER_X:
            return -1  # Player (X) wins
        elif winner == 0:
            return 0  # Tie

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i, j] == EMPTY:
                        self.board[i, j] = PLAYER_O
                        score = self.minimax(depth + 1, False)
                        self.board[i, j] = EMPTY
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i, j] == EMPTY:
                        self.board[i, j] = PLAYER_X
                        score = self.minimax(depth + 1, True)
                        self.board[i, j] = EMPTY
                        best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -float('inf')
        move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == EMPTY:
                    self.board[i, j] = PLAYER_O
                    score = self.minimax(0, False)
                    self.board[i, j] = EMPTY
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def play_game(self):
        while True:
            self.print_board()
            if self.current_player == PLAYER_X:
                row, col = map(int, input("Enter your move (row and column): ").split())
                self.make_move(row, col)
            else:
                print("AI is making a move...")
                row, col = self.best_move()
                self.make_move(row, col)

            winner = self.check_winner()
            if winner is not None:
                self.print_board()
                if winner == PLAYER_X:
                    print("Player X wins!")
                elif winner == PLAYER_O:
                    print("Player O (AI) wins!")
                else:
                    print("It's a tie!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
