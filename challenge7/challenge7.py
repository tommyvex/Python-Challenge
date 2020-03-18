from PIL import Image

pic = Image.open('oxygen.png')
width, height = pic.size
pic_pixel = pic.getpixel((0, height//2))

#The chr() returns: a character (a string) whose Unicode code point is the integer i. If the integer i is outside the range, ValueError will be raised.
#print((chr(115), chr(255)))

#print pixels from int to char?!

pixel_return = [chr(pic.getpixel((i, height//2))[0]) for i in range(0, width, 7)]
#colors change every 7 pixels so range(0, width, 7)
print("".join(pixel_return))

print("".join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121])))