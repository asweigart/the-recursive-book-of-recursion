# NOTE https://solarianprogrammer.com/2017/11/20/eight-queens-puzzle-python/
SIZE = 8
numSolutions = 0

def placeQueenOnRow(board, row):
    global numSolutions
    if row == SIZE:
        # BASE CASE
        printBoard(board)
        numSolutions += 1
    else:
        # Test potential column against previously placed queens:
        for column in range(SIZE):
            columnIsValid = True
            for i in range(row):
                # Is in the same column as another queen:
                sameColumn = board[i] == column
                # On the same / diagonal:
                sameForwardDiag = board[i] + i == column + row
                # On the same \ diagonal:
                sameBackwardDiag = board[i] - i == column - row
                if sameColumn or sameForwardDiag or sameBackwardDiag:
                    columnIsValid = False
                    break

            if columnIsValid:
                # RECURSIVE CASE
                # Place a queen in this column on this row:
                board[row] = column
                # Place a queen on the next row:
                placeQueenOnRow(board, row + 1)
        # By now, all possible columns on this row have been tried.

def printBoard(board):
    for row in range(SIZE):
        line = ''
        for column in range(SIZE):
            if board[row] == column:
                line += 'Q '  # Display a queen.
            else:
                line += '. '  # Display a blank space.
        print(line)
    print('\n')

# ['column of queen in row 0', 'column of queen in row 1', etc...]
board = [None] * SIZE
placeQueenOnRow(board, 0)
print('Number of solutions:', numSolutions)
