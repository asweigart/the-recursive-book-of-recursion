import random, time

#random.seed(42)  # Select which puzzle to solve.
SIZE = 4  # Set this to either 3 or 4.
BLANK = 0

# Constants for directions:
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'



def displayBoard(board):
    """Display `board` on the screen."""

    for y in range(SIZE):  # Iterate over each row.
        for x in range(SIZE):  # Iterate over each column.
            if board[y * SIZE + x] == BLANK:
                print('__ ', end='')
            else:
                print(str(board[y * SIZE + x]).rjust(2) + ' ', end='')

        print()  # Print a newline at the end of the row.





def getNewBoard():
    """Return a list of lists that represents a new tile puzzle."""
    # NOTE: All the single digit numbers have a space in front of them.
    return list(range(1, SIZE * SIZE)) + [BLANK]


def findBlankSpace(board):
    """Return an [x, y] list of the blank space's location."""
    for x in range(SIZE):
        for y in range(SIZE):
            if board[y * SIZE + x] == BLANK:
                return [x, y]






def makeMove(board, move):
    """Carry out the given move on the given board in `board`."""

    bx, by = findBlankSpace(board)
    blankIndex = by * SIZE + bx

    if move == UP:
        tileIndex = (by + 1) * SIZE + bx
    elif move == LEFT:
        tileIndex = by * SIZE + (bx + 1)
    elif move == DOWN:
        tileIndex = (by - 1) * SIZE + bx
    elif move == RIGHT:
        tileIndex = by * SIZE + (bx - 1)

    board[blankIndex], board[tileIndex] = board[tileIndex], board[blankIndex]




def undoMove(board, move):
    """Do the opposite move of `move` to undo it on `board`."""
    if move == UP:
        makeMove(board, DOWN)
    elif move == DOWN:
        makeMove(board, UP)
    elif move == LEFT:
        makeMove(board, RIGHT)
    elif move == RIGHT:
        makeMove(board, LEFT)




def getValidMoves(board):
    """Returns a list of the valid moves to make on this board."""

    blankx, blanky = findBlankSpace(board)

    validMoves = []
    if blanky != SIZE - 1:  # Blank space is not on the bottom row.
        validMoves.append(UP)

    if blankx != SIZE - 1:  # Blank space is not on the right column.
        validMoves.append(LEFT)

    if blanky != 0:  # Blank space is not on the top row.
        validMoves.append(DOWN)

    if blankx != 0:  # Blank space is not on the left column.
        validMoves.append(RIGHT)

    return validMoves



def getNewPuzzle():
    """Get a new puzzle by making random slides from a solved state."""
    board = getNewBoard()
    for i in range(50):
        validMoves = getValidMoves(board)
        makeMove(board, random.choice(validMoves))

    return board


def solve(board, maxMoves):
    """Attempt to solve the puzzle in `board` in at most `maxMoves`
    moves. Returns True if solved, otherwise False."""
    print('Attempting to solve in at most', maxMoves, 'moves...')
    solutionMoves = []  # A list of UP, DOWN, LEFT, RIGHT values.
    cache = set()
    hitsMisses = {'hits': 0, 'misses': 0}
    st = time.time()
    solved = attemptMove(board, solutionMoves, cache, hitsMisses, maxMoves, 0)
    duration = round(time.time() - st, 2)
    if solved:
        displayBoard(board)
        for move in solutionMoves:
            print('Move', move)
            makeMove(board, move)
            print()  # Print a newline.
            displayBoard(board)
            print()  # Print a newline.

        print('Solved in', len(solutionMoves), 'moves:')
        print(', '.join(solutionMoves))
        #_log(maxMoves, duration, hitsMisses)
        #input('debug: check memory')
        return True  # Puzzle was solved.
    else:
        #_log(maxMoves, duration, hitsMisses)
        #input('debug: check memory')
        return False  # Unable to solve in maxMoves moves.


def _log(maxMoves, duration, hitsMisses):
    with open('_log.csv', 'a') as fo:
        fo.write(str(maxMoves) + '\t' + str(round(duration, 1)) + '\t' + str(hitsMisses['hits']) + '\t' + str(hitsMisses['misses']) + '\t' + str(round(hitsMisses['hits'] / (hitsMisses['hits'] + hitsMisses['misses']) * 100, 2)) + '%\n')
        print(str(maxMoves) + '\t' + str(round(duration, 1)) + '\t' + str(hitsMisses['hits']) + '\t' + str(hitsMisses['misses']) + '\t' + str(round(hitsMisses['hits'] / (hitsMisses['hits'] + hitsMisses['misses']) * 100, 2)) + '%')

def attemptMove(board, movesMade, stateCache, cacheHitsMisses, maxMoves, depth):
    """A recursive function that attempts all possible moves on `board`
    until a solution is found or we've reached the `maxMoves` limit.
    Returns True if a solution was found, in which case, movesMade
    contains the series of moves to solve the puzzle. Returns False
    if no solution was found in `maxMoves` moves."""

    if depth > maxMoves:
        return False  # BASE CASE

    if board == SOLVED_BOARD:
        # BASE CASE - Solved the puzzle:
        return True

    boardAsBytes = bytes(board)
    if boardAsBytes in stateCache:
        cacheHitsMisses['hits'] += 1
        return False
    else:
        cacheHitsMisses['misses'] += 1
    stateCache.add(boardAsBytes)

    # Attempt each of the valid moves:
    for move in getValidMoves(board):
        # Make the move:
        makeMove(board, move)
        movesMade.append(move)

        # RECURSIVE CASE - Attempt another move:
        if attemptMove(board, movesMade, stateCache, cacheHitsMisses, maxMoves, depth + 1):
            # If the puzzle is solved, return True:
            undoMove(board, move)
            return True

        # Undo this last move to set up for the next move:
        undoMove(board, move)
        movesMade.pop()  # Remove the last move since it was undone.

    return False  # BASE CASE - Unable to find a solution.



# Start the program:
SOLVED_BOARD = getNewBoard()
gameBoard = getNewPuzzle()
displayBoard(gameBoard)
startTime = time.time()

maxMoves = 10
while True:
    if solve(gameBoard, maxMoves):
        break  # Break out of the loop when a solution is found.
    maxMoves += 1
print('Run in', round(time.time() - startTime, 1), 'seconds.')
