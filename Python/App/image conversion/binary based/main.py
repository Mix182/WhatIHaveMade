from PIL import Image

img = Image.open("image.jpeg")

def rcv(number, x, max_number=255):
    y = max_number / x
    for i in range(x):
        if number >= i * y and number <= (i + 1) * y:
            return int(i * y)

    print(number)
    
    

width, height = img.size

z = int(input("N of states, that: r, g, or b value can be:\n"))

for x in range(width):
    for y in range(height):
        pixel = img.getpixel((x, y))
        
        r = rcv(pixel[0], z)
        g = rcv(pixel[1], z)
        b = rcv(pixel[2], z)
        img.putpixel((x, y), (r, g, b))

img.show()
print(f"Number of colors used:\n{z ** 3}")