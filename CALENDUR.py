from PIL import Image

# create image transparent bkg
width = 1728
height = 1728
grid_image = Image.new('RGBA', (width, height), (255, 255, 255, 0))



# have text file with python dict that houses what each grid are is
# for loop (for each item in dict)

A = Image.open("A.png")
B = Image.open("B.png")
C = Image.open("C.png")
D = Image.open("D.png")
E = Image.open("E.png")
F = Image.open("F.png")
G = Image.open("G.png")
H = Image.open("H.png")
I = Image.open("I.png")
# ... continue for all needed images






image_1 = A
image_2 = B
image_3 = C
image_4 = D
image_5 = E
image_6 = F
image_7 = G
image_8 = H
image_9 = I

cell_width = int(width / 3)
cell_height = int(height / 3)

#place images in grid
grid_image.paste(image_1, (0, 0))
grid_image.paste(image_2, (cell_width, 0))
grid_image.paste(image_3, (cell_width * 2, 0))
grid_image.paste(image_4, (0, cell_height))
grid_image.paste(image_5, (cell_width, cell_height))
grid_image.paste(image_6, (cell_width * 2, cell_height))
grid_image.paste(image_7, (0, cell_height * 2))
grid_image.paste(image_8, (cell_width, cell_height * 2))
grid_image.paste(image_9, (cell_width * 2, cell_height * 2))


grid_image.save("grid.png")
#varrible that hs day # in it
