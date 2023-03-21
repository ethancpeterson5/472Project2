import stateHelpers

currentBoard = []
def main():
    initMatrix()
    printMatrix(currentBoard)
    print(stateHelpers.getMoves(currentBoard, 'L'))

def initMatrix():
    global currentBoard
    currentBoard = [['_' for i in range(8)] for j in range(8)]
    currentBoard[3][3] = "L"
    currentBoard[3][4] = 'D'
    currentBoard[4][3] = 'D'
    currentBoard[4][4] = 'L'
def printMatrix(currentBoard):
    print("0  1  2  3  4  5  6  7")
    for row in range(len(currentBoard)):
        for column in range(len(currentBoard[row])):
            print(currentBoard[row][column] + ' ', end=" ")
        print(row)
    print()

if __name__ == "__main__":
    main()