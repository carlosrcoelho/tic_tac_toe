from enum import Enum
import random

class Player(Enum):
    X = "X"
    O = "O"
    EMPTY = " "

def printGameBoard(game_board):
    for row in game_board:
        print("+---+---+---+")
        print("| {} | {} | {} |".format(row[0], row[1], row[2]))
    print("+---+---+---+")

def modifyArray(game_board, num, turn):
    row = (num - 1) // 3
    col = (num - 1) % 3
    if game_board[row][col] == Player.EMPTY.value:
        game_board[row][col] = turn
        return True
    else:
        print("Invalid move. Cell already occupied.")
        return False

def checkWinner(game_board):
    for row in game_board:
        if row[0] == row[1] == row[2] != Player.EMPTY.value:
            return row[0]
    
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] != Player.EMPTY.value:
            return game_board[0][col]
    
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != Player.EMPTY.value or \
       game_board[0][2] == game_board[1][1] == game_board[2][0] != Player.EMPTY.value:
        return game_board[1][1]
    
    return Player.EMPTY.value

def isBoardFull(game_board):
    for row in game_board:
        if Player.EMPTY.value in row:
            return False
    return True

def main():
    print("Welcome to Tic Tac Toe!")
    print("-----------------------")

    gameBoard = [[Player.EMPTY.value for _ in range(3)] for _ in range(3)]
    possible_moves = [i for i in range(1, 10)]
    turnCount = 0

    while True:
        printGameBoard(gameBoard)

        if turnCount % 2 == 0:
            number_picked = int(input("Pick a number from 1-9: "))
            if number_picked in possible_moves:
                if modifyArray(gameBoard, number_picked, Player.X.value):
                    possible_moves.remove(number_picked)
                    turnCount += 1
            else:
                print("Invalid number, try again")
        else:
            cpuChoice = random.choice(possible_moves)
            if modifyArray(gameBoard, cpuChoice, Player.O.value):
                possible_moves.remove(cpuChoice)
                turnCount += 1
            else:
                continue

        winner = checkWinner(gameBoard)
        if winner != Player.EMPTY.value:
            printGameBoard(gameBoard)
            print(f"{winner} wins!")
            break
        elif isBoardFull(gameBoard):
            printGameBoard(gameBoard)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
