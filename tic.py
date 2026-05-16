class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current = "X"

    def show(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6: print("--+---+--")
        print()

    def winner(self):
        wins = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
        for a,b,c in wins:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        return "Draw" if " " not in self.board else None

    def switch(self):
        self.current = "O" if self.current == "X" else "X"

    def minimax(self, turn):
        result = self.winner()
        if result == self.ai: return 1
        if result == self.human: return -1
        if result == "Draw": return 0

        scores = []
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = turn
                scores.append(self.minimax(self.human if turn==self.ai else self.ai))
                self.board[i] = " "
        return max(scores) if turn == self.ai else min(scores)

    def best_move(self):
        best, move = -999, 0
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.ai
                score = self.minimax(self.human)
                self.board[i] = " "
                if score > best:
                    best, move = score, i
        return move

    def play(self):
        mode = input("1: Human vs Human\n2: Human vs AI\nChoose: ")
        if mode == "2":
            self.human = input("Choose X or O: ").upper()
            self.ai = "O" if self.human == "X" else "X"

        while True:
            self.show()
            if self.winner():
                print(self.winner(), "wins!" if self.winner()!="Draw" else "")
                break

            if mode=="2" and self.current==self.ai:
                print("Computer thinking...")
                move = self.best_move()
            else:
                move = int(input(f"{self.current} move (0-8): "))

            if self.board[move]==" ":
                self.board[move]=self.current
                self.switch()
            else:
                print("Invalid!")

game = TicTacToe()
game.play()