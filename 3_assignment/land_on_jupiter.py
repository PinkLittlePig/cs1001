import random

def createGameBoard(rows, columns):
    board = []
    for row in range(rows):
        row = []
        for column in range(columns):
            row.append(random.randint(50, 99))
        board.append(row)
    return board

def makeACopy(gameBoard):
    newCopy = []
    for row in gameBoard:
        newCopy.append(row[:])
    return newCopy

def printBoard(gameBoard):
    for row in gameBoard:
        print("|", end="")
        print(("{:<2}|"*len(row)).format(*row))

def collectGummies(gameBoard):
    collectedGummies = [0, 0]
    for turn in range(5):
        for player in range(1, 3):
            playerOneRow = int(input(f"Player {player}, enter your row number: (1-10)"))-1
            randomColumn = random.randint(0, 5)
            collectedGummies[player-1] += gameBoard[playerOneRow][randomColumn]
            gameBoard[playerOneRow][randomColumn] = 0
            print(f"Player {player}, your randomly chosen column is {randomColumn} so you get {collectedGummies[player-1]} gummy bears.")

    return collectedGummies

def main():
    playerOneName = input("Enter the name of player 1: ")
    playerTwoName = input("Enter the name of player 2: ")
    
    gameBoard = createGameBoard(10, 6)
    originalGameBoard = makeACopy(gameBoard)
    scores = collectGummies(gameBoard)
    
    printBoard(originalGameBoard)
    printBoard(gameBoard)
    print(scores)


if __name__ == "__main__":
    main()
