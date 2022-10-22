SIZE = 8

def getPermutations(items):
    if len(items) == 0:
        # BASE CASE
        return [[]]
    else:
        # RECURSIVE CASE
        permutations = []
        head = [items[0]]
        tail = items[1:]
        tailPermutations = getPermutations(tail)
        for tailPerm in tailPermutations:
            for i in range(len(tailPerm) + 1):
                newPermutation = tailPerm[0:i] + head + tailPerm[i:]
                permutations.append(newPermutation)
        return permutations

def printBoard(board):
    for row in range(SIZE):
        for column in range(SIZE):
            if board[row] == column:
                print('Q ', end='')
            else:
                print('. ', end='')
        print()
    print()

#print(getPermutations(list(range(SIZE))))
numSolutions = 0
for board in getPermutations(list(range(SIZE))):
    # check if any queens can diagonally attack each other
    isValidBoard = True
    for row, column in enumerate(board):
        for otherRow, otherColumn in enumerate(board):
            if (row, column) == (otherRow, otherColumn):
                continue
            sameForwardDiagonal  = row + column == otherRow + otherColumn # On the same / diagonal.
            sameBackwardDiagonal = column - row == otherColumn - otherRow # On the same \ diagonal.
            if sameForwardDiagonal or sameBackwardDiagonal:
                isValidBoard = False
                break

    if isValidBoard:
        printBoard(board)
        numSolutions += 1
print('Number of solutions:', numSolutions)
