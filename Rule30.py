from PIL import Image

BLACK = 0
WHITE = 1
WIDTH = 256
HEIGHT = int(WIDTH/2)

CENTER_WIDTH = int(WIDTH/2)

img = Image.new("1", (WIDTH, HEIGHT), WHITE)
img.putpixel((CENTER_WIDTH, 0), BLACK)
#img.putpixel((0, 0), BLACK)

for y in range(1, HEIGHT):
    for x in range(0, WIDTH):
        if x == 0:
            topLeft = WHITE
        else:
            topLeft = img.getpixel((x-1, y-1))

        topMiddle = img.getpixel((x, y-1))

        if x == WIDTH - 1:
            topRight = WHITE
        else:
            topRight = img.getpixel((x+1, y-1))
        
        if topLeft == BLACK and topMiddle == BLACK and topRight == BLACK:
            img.putpixel((x, y), WHITE)

        elif topLeft == BLACK and topMiddle == BLACK and topRight == WHITE:
            img.putpixel((x, y), WHITE)

        elif topLeft == BLACK and topMiddle == WHITE and topRight == BLACK:
            img.putpixel((x, y), WHITE)

        elif topLeft == BLACK and topMiddle == WHITE and topRight == WHITE:
            img.putpixel((x, y), BLACK)

        elif topLeft == WHITE and topMiddle == BLACK and topRight == BLACK:
            img.putpixel((x, y), BLACK)

        elif topLeft == WHITE and topMiddle == BLACK and topRight == WHITE:
            img.putpixel((x, y), BLACK)

        elif topLeft == WHITE and topMiddle == WHITE and topRight == BLACK:
            img.putpixel((x, y), BLACK)

        elif topLeft == WHITE and topMiddle == WHITE and topRight == WHITE:
            img.putpixel((x, y), WHITE)
    filename = "test%s.jpg"%y
    img.save(filename)