# Tic Tac Toe (Console)
# Supports:
#  - Human vs Human
#  - Human vs Computer (Minimax AI - plays optimally)

from typing import List, Optional, Tuple

BOARD_INDICES = """
Board positions:
 0 | 1 | 2
---+---+---
 3 | 4 | 5
---+---+---
 6 | 7 | 8
"""

WIN_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diagonals
]


def print_board(board: List[str]) -> None:
    """Print the Tic Tac Toe board nicely."""
    def v(i): return board[i] if board[i] != " " else str(i)
    print(f" {v(0)} | {v(1)} | {v(2)} ")
    print("---+---+---")
    print(f" {v(3)} | {v(4)} | {v(5)} ")
    print("---+---+---")
    print(f" {v(6)} | {v(7)} | {v(8)} ")


def check_winner(board: List[str]) -> Optional[str]:
    """Return 'X' or 'O' if there's a winner, 'D' for draw, or None if game ongoing."""
    for a, b, c in WIN_COMBINATIONS:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if all(cell != " " for cell in board):
        return "D"  # Draw
    return None


def available_moves(board: List[str]) -> List[int]:
    return [i for i, v in enumerate(board) if v == " "]


def minimax(board: List[str], current_player: str, ai_player: str, human_player: str) -> Tuple[int, Optional[int]]:
    """
    Minimax algorithm.
    Returns (score, move_index)
    Score: +1 if ai_player wins, -1 if human_player wins, 0 draw.
    """
    winner = check_winner(board)
    if winner == ai_player:
        return 1, None
    elif winner == human_player:
        return -1, None
    elif winner == "D":
        return 0, None

    moves = available_moves(board)
    best_move = None

    if current_player == ai_player:
        # maximize
        best_score = -999
        for m in moves:
            board[m] = current_player
            score, _ = minimax(board, human_player, ai_player, human_player)
            board[m] = " "
            if score > best_score:
                best_score = score
                best_move = m
        return best_score, best_move
    else:
        # minimize
        best_score = 999
        for m in moves:
            board[m] = current_player
            score, _ = minimax(board, ai_player, ai_player, human_player)
            board[m] = " "
            if score < best_score:
                best_score = score
                best_move = m
        return best_score, best_move


def get_ai_move(board: List[str], ai_player: str, human_player: str) -> int:
    """Return best move for AI using minimax. If first move, prefer center."""
    # If board is empty, pick center for a stronger start
    if board.count(" ") == 9:
        return 4
    _, move = minimax(board, ai_player, ai_player, human_player)
    assert move is not None
    return move


def human_move(board: List[str], player: str) -> None:
    """Prompt human to make a move; modifies board in place."""
    moves = available_moves(board)
    while True:
        try:
            choice = input(f"Player {player}, enter your move (0-8) or 'b' to view board indices: ").strip()
            if choice.lower() == 'b':
                print(BOARD_INDICES)
                continue
            pos = int(choice)
            if pos in moves:
                board[pos] = player
                return
            else:
                print("Invalid move — position already taken or out of range. Try again.")
        except ValueError:
            print("Please enter a number between 0 and 8, or 'b' to view indices.")


def choose_option(prompt: str, options: List[str]) -> str:
    """Helper to choose an option from provided choices."""
    options_str = "/".join(options)
    while True:
        choice = input(f"{prompt} ({options_str}): ").strip().upper()
        if choice in options:
            return choice
        print("Invalid option. Try again.")


def play_game():
    print("Welcome to Tic Tac Toe!")
    print(BOARD_INDICES)
    mode = choose_option("Choose mode: Human vs Human (H) or Human vs Computer (C)?", ["H", "C"])
    player_X = "X"
    player_O = "O"

    # Let human choose symbol if playing vs AI
    if mode == "C":
        human_symbol = choose_option("Pick your symbol X or O?", ["X", "O"])
        ai_symbol = "O" if human_symbol == "X" else "X"
    else:
        human_symbol = None
        ai_symbol = None

    # Who goes first?
    first = choose_option("Who goes first? X or O?", ["X", "O"])
    current = first

    board = [" "] * 9
    print_board(board)

    while True:
        winner = check_winner(board)
        if winner is not None:
            if winner == "D":
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            print_board(board)
            break

        if mode == "H":
            # Both human players
            human_move(board, current)
        else:
            # Human vs AI
            if current == human_symbol:
                human_move(board, current)
            else:
                print(f"Computer ({ai_symbol}) is making a move...")
                move = get_ai_move(board, ai_symbol, human_symbol)
                board[move] = ai_symbol

        print()
        print_board(board)
        print()

        # switch player
        current = "O" if current == "X" else "X"
        again = input("Play again ? (yes/no): ")
        if again.lower() != "yes":
            break

if __name__ == "__main__":
    play_game()
