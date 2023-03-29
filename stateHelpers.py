def getMoves(currentBoard, move):
    moves = []
    for i in range(8):
        for j in range(8):
            if currentBoard[i][j] == '_':
                if checkIfMoveCaptures(currentBoard, i,j,move):
                    moves.append([i,j])
    return moves

def checkIfMoveCaptures(currentBoard, i, j, move):
    captured = False
    if move == 'L':
        oppositeMove = 'R'
    else:
        oppositeMove = 'L'
    for changeInI in range(-1,2):
        for changeInJ in range(-1,2):
            if changeInI == 0 and changeInJ == 0:
                continue
            row = i + changeInI
            col = j + changeInJ
            while 0 <= row < 8 and 0 <= col < 8 and currentBoard[row][col] != '_':
                if currentBoard[row][col] == move:
                    captured = True
                    break
                row += changeInI
                col += changeInJ
            if captured:
                return True

    return False