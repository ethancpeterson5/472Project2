def getMoves(currentBoard, move):
    moves = []
    for i in range(len(currentBoard)):
        for j in range(len(currentBoard[0])):
            if(currentBoard[i][j] != 'L' or currentBoard[i][j] != 'D'):
                if(i >= 2):
                    if(currentBoard[i-2][j] == move):
                        moves.append([i-2,j])
                if(i <= 5):
                    if(currentBoard[i+2][j] == move):
                        moves.append([i+2,j])
                if (j >= 2):
                    if (currentBoard[i][j - 2] == move):
                        moves.append([i, j - 2])
                if (j <= 5):
                    if (currentBoard[i][j + 2] == move):
                        moves.append([i, j + 2])