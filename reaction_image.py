from PIL import Image, ImageGrab 
im1 = Image.open("live_reaction.png")


im2 = ImageGrab.grabclipboard() 
im3 = im2.resize((930, 530))
im4 = im2.resize((300, 100))


Image.Image.paste(im1, im3, (15, 162))
Image.Image.paste(im1, im4, (210, 30))

im1.show()
