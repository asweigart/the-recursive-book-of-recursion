# Set up towers A, B, and C. The end of the list is the top of the tower.
TOTAL_DISKS = 3

# Populate Tower A:
TOWERS = {'A': list(reversed(range(1, TOTAL_DISKS + 1))),
          'B': [],
          'C': []}

def printDisk(diskNum):
    # Print a single disk of width diskNum.
    emptySpace = ' ' * (TOTAL_DISKS - diskNum)
    if diskNum == 0:
        # Just draw the pole.
        print(emptySpace + '||' + emptySpace, end='')
    else:
        # Draw the disk.
        diskSpace = '@' * diskNum
        diskNumLabel = str(diskNum).rjust(2, '_')
        print(emptySpace + diskSpace + diskNumLabel + diskSpace + emptySpace, end='')

def printTowers():
    # Print all three towers.
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if level >= len(tower):
                printDisk(0)
            else:
                printDisk(tower[level])
        print()
    # Print the tower labels A, B, and C.
    emptySpace = ' ' * (TOTAL_DISKS)
    print('%s A%s%s B%s%s C\n' % (emptySpace, emptySpace, emptySpace, emptySpace, emptySpace))

def moveOneDisk(startTower, endTower):
    # Move the top disk from startTower to endTower.
    disk = TOWERS[startTower].pop()
    TOWERS[endTower].append(disk)

def solveIterative(numberOfDisks, startTower, endTower, tempTower):
    tasks = [[numberOfDisks, startTower, endTower, tempTower, '1st step']]

    while tasks:
        numberOfDisks, startTower, endTower, tempTower, instrPtr = tasks[-1] # read local vars off the top of the stack

        # Move the top numberOfDisks disks from startTower to endTower.
        if numberOfDisks == 1:
            # BASE CASE
            moveOneDisk(startTower, endTower)
            printTowers()
            tasks.pop()
            continue
        else:
            # RECURSIVE CASE
            if instrPtr == '1st step':
                tasks[-1][4] = '2nd step'
                tasks.append([numberOfDisks - 1, startTower, tempTower, endTower, '1st step'])
                continue
            elif instrPtr == '2nd step':
                moveOneDisk(startTower, endTower)
                printTowers()
                tasks[-1][4] = '3rd step'
                tasks.append([numberOfDisks - 1, tempTower, endTower, startTower, '1st step'])
                continue
            elif instrPtr == '3rd step':
                tasks.pop()
                continue

def solveRecursive(numberOfDisks, startTower, endTower, tempTower):
    # Move the top numberOfDisks disks from startTower to endTower.
    if numberOfDisks == 1:
        # BASE CASE
        moveOneDisk(startTower, endTower)
        printTowers()
        return
    else:
        # RECURSIVE CASE
        solveRecursive(numberOfDisks - 1, startTower, tempTower, endTower)
        moveOneDisk(startTower, endTower)
        printTowers()
        solveRecursive(numberOfDisks - 1, tempTower, endTower, startTower)
        return

# Solve
printTowers()
solveIterative(TOTAL_DISKS, 'A', 'B', 'C')

# Uncomment to enable interactive mode:
#while True:
#    printTowers()
#    print('Enter letter of start tower and the end tower. (A, B, C) Or Q to quit.')
#    move = input().upper()
#    if move == 'Q':
#        sys.exit()
#    elif move[0] in 'ABC' and move[1] in 'ABC' and move[0] != move[1]:
#        moveOneDisk(move[0], move[1])

