import sys

# Create the image (make sure it's rectangular!)
im = [list('..########################...........'),
      list('..#......................#...#####...'),
      list('..#..........########....#####...#...'),
      list('..#..........#......#............#...'),
      list('..#..........########.........####...'),
      list('..######......................#......'),
      list('.......#..#####.....###########......'),
      list('.......####...#######................')]

HEIGHT = len(im)
WIDTH = len(im[0])

def floodFill(image, x, y, newChar):
    oldChar = image[y][x]
    pixelsToCheck = [[x, y]]

    while len(pixelsToCheck) > 0:
      x, y = pixelsToCheck.pop()
      if oldChar == newChar or image[y][x] != oldChar:
          # BASE CASE
          continue

      image[y][x] = newChar # Change the character.

      # Uncomment to view each step:
      #printImage(image)

      # Change the neighboring characters.
      if y + 1 < HEIGHT and image[y + 1][x] == oldChar:
          # RECURSIVE CASE
          pixelsToCheck.append([x, y + 1])
      if y - 1 >= 0 and image[y - 1][x] == oldChar:
          # RECURSIVE CASE
          pixelsToCheck.append([x, y - 1])
      if x + 1 < WIDTH and image[y][x + 1] == oldChar:
          # RECURSIVE CASE
          pixelsToCheck.append([x + 1, y])
      if x - 1 >= 0 and image[y][x - 1] == oldChar:
          # RECURSIVE CASE
          pixelsToCheck.append([x - 1, y])

def printImage(image):
    for y in range(HEIGHT):
        # Print each row.
        for x in range(WIDTH):
            # Print each column.
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')

printImage(im)
floodFill(im, 3, 3, 'o')
printImage(im)
