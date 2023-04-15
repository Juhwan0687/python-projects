from PIL import Image

img=Image.open('fruit.jpeg')

img_rotate=img.rotate(270)
img_convert=img.convert('L')

img_convert.save('Fruit black.png')
img_rotate.save('Fruit rotate.png')

img_rotate.show()
img_convert.show()