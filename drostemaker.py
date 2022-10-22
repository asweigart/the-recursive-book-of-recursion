from PIL import Image


def makeDroste(baseImage, stopAfter=10):
    # If baseImage is a string of an image filename, load that image:
    if isinstance(baseImage, str):
        baseImage = Image.open(baseImage)

    if stopAfter == 0:
        # BASE CASE
        return baseImage

    # The magenta color has max red/blue/alpha, zero green:
    if baseImage.mode == 'RGBA':
        magentaColor = (255, 0, 255, 255)
    elif baseImage.mode == 'RGB':
        magentaColor = (255, 0, 255)

    # Find the dimensions of the base image and its magenta area:
    baseImageWidth, baseImageHeight = baseImage.size
    magentaLeft = None
    magentaRight = None
    magentaTop = None
    magentaBottom = None

    for x in range(baseImageWidth):
        for y in range(baseImageHeight):
            if baseImage.getpixel((x, y)) == magentaColor:
                if magentaLeft is None or x < magentaLeft:
                    magentaLeft = x
                if magentaRight is None or x > magentaRight:
                    magentaRight = x
                if magentaTop is None or y < magentaTop:
                    magentaTop = y
                if magentaBottom is None or y > magentaBottom:
                    magentaBottom = y

    if magentaLeft is None:
        # BASE CASE - No magenta pixels are in the image.
        return baseImage

    # Get a resized version of the base image:
    magentaWidth = magentaRight - magentaLeft + 1
    magentaHeight = magentaBottom - magentaTop + 1
    baseImageAspectRatio = baseImageWidth / baseImageHeight
    magentaAspectRatio = magentaWidth / magentaHeight

    if baseImageAspectRatio < magentaAspectRatio:
        # Make the resized width match the width of the magenta area:
        widthRatio = magentaWidth / baseImageWidth
        resizedImage = baseImage.resize((magentaWidth,
        int(baseImageHeight * widthRatio) + 1), Image.NEAREST)
    else:
        # Make the resized height match the height of the magenta area:
        heightRatio =  magentaHeight / baseImageHeight
        resizedImage = baseImage.resize((int(baseImageWidth *
        heightRatio) + 1, magentaHeight), Image.NEAREST)

    # Replace the magenta pixels with the smaller, resized image:
    for x in range(magentaLeft, magentaRight + 1):
        for y in range(magentaTop, magentaBottom + 1):
            if baseImage.getpixel((x, y)) == magentaColor:
                pix = resizedImage.getpixel((x - magentaLeft, y - magentaTop))
                baseImage.putpixel((x, y), pix)

    # RECURSIVE CASE:
    return makeDroste(baseImage, stopAfter=stopAfter - 1)


recursiveImage = makeDroste('museum.png')
recursiveImage.save('museum-recursive.png')
recursiveImage.show()
