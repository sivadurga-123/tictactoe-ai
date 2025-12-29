class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.human = 'O'
        self.ai = 'X'

    def print_board(self):
        """Print the board in a readable format"""
        print('\n')
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print('\n')

    def is_winner(self, player):
        """Check if a player has won"""
        win_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]               # diagonals
        ]
        return any(all(self.board[i] == player for i in combo) for combo in win_combos)

    def is_board_full(self):
        """Check if the board is full"""
        return ' ' not in self.board

    def get_empty_cells(self):
        """Get list of empty cells"""
        return [i for i, cell in enumerate(self.board) if cell == ' ']

    def minimax(self, depth, is_maximizing, alpha=float('-inf'), beta=float('inf')):
        """Minimax algorithm with Alpha-Beta pruning"""
        if self.is_winner(self.ai):
            return 10 - depth
        if self.is_winner(self.human):
            return depth - 10
        if self.is_board_full():
            return 0

        if is_maximizing:
            max_eval = float('-inf')
            for cell in self.get_empty_cells():
                self.board[cell] = self.ai
                eval_score = self.minimax(depth + 1, False, alpha, beta)
                self.board[cell] = ' '
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for cell in self.get_empty_cells():
                self.board[cell] = self.human
                eval_score = self.minimax(depth + 1, True, alpha, beta)
                self.board[cell] = ' '
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval

    def ai_move(self):
        """AI makes the best move using minimax algorithm"""
        best_score = float('-inf')
        best_move = None
        for cell in self.get_empty_cells():
            self.board[cell] = self.ai
            score = self.minimax(0, False)
            self.board[cell] = ' '
            if score > best_score:
                best_score = score
                best_move = cell
        if best_move is not None:
            self.board[best_move] = self.ai
            return best_move

    def human_move(self, position):
        """Human player makes a move"""
        if self.board[position] == ' ':
            self.board[position] = self.human
            return True
        return False

    def play(self):
        """Main game loop"""
        print("Welcome to Tic-Tac-Toe!")
        print("You are O, AI is X")
        print("Positions are numbered 0-8:")
        print("0 | 1 | 2")
        print("---------")
        print("3 | 4 | 5")
        print("---------")
        print("6 | 7 | 8")
        
        while True:
            self.print_board()
            
            # Human move
            while True:
                try:
                    pos = int(input("Enter your move (0-8): "))
                    if 0 <= pos <= 8 and self.human_move(pos):
                        break
                    print("Invalid move! Try again.")
                except ValueError:
                    print("Please enter a number between 0-8.")
            
            if self.is_winner(self.human):
                self.print_board()
                print("Congratulations! You won!")
                break
            
            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break
            
            # AI move
            print("AI is thinking...")
            self.ai_move()
            
            if self.is_winner(self.ai):
                self.print_board()
                print("AI wins! Game over.")
                break
            
            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break

if __name__ == '__main__':
    game = TicTacToe()
    game.play()
