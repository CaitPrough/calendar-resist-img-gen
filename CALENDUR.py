from PIL import Image
import os
from formatted_dates import formatted_dates

# create image transparent bkg
width = 2048
height = 2048
grid_image = Image.new('RGBA', (width, height), (255, 255, 255, 0))



# have text file with python dict that houses what each grid are is
# for loop (for each item in dict)

#X IS A BLANK SPACE
A = Image.open("A.png")
B = Image.open("B.png")
C = Image.open("C.png")
D = Image.open("D.png")
E = Image.open("E.png")
F = Image.open("F.png")
G = Image.open("G.png")
H = Image.open("H.png")
I = Image.open("I.png")
J = Image.open("J.png")
L = Image.open("L.png")
M = Image.open("M.png")
N = Image.open("N.png")
O = Image.open("O.png")
P = Image.open("P.png")
R = Image.open("R.png")
S = Image.open("S.png")
T = Image.open("T.png")
U = Image.open("U.png")
V = Image.open("V.png")
W = Image.open("W.png")
zero = Image.open("0.png")
one = Image.open("1.png")
two = Image.open("2.png")
three = Image.open("3.png")
four = Image.open("4.png")
five = Image.open("5.png")
six = Image.open("6.png")
seven = Image.open("7.png")
eight = Image.open("8.png")
nine = Image.open("9.png")
blank = Image.open("blank.png")
# ... continue for all needed images

def determineN(x):
    if x == '0':
        y = zero
        
    elif x == '1':
        y = one
        
    elif x == '2':
        y = two
        
    elif x == '3':
        y = three
        
    elif x == '4':
        y = four
     
    elif x == '5':
        y = five
        
    elif x == '6':
        y = six
        
    elif x == '7':
        y = seven
        
    elif x == '8':
        y = eight
    
    elif x == '9':
        y = nine
        
    else:
        y = blank
        
    return y

def determineL(x):
    if x == 'A':
        y = A
        
    elif x == 'B':
        y = B
        
    elif x == 'C':
        y = C
        
    elif x == 'D':
        y = D
        
    elif x == 'E':
        y = E
     
    elif x == 'F':
        y = F
        
    elif x == 'G':
        y = G
        
    elif x == 'H':
        y = H
        
    elif x == 'I':
        y = I
    
    elif x == 'J':
        y = J
        
    elif x == 'L':
        y = L
        
    elif x == 'M':
        y = M
        
    elif x == 'N':
        y = N
     
    elif x == 'O':
        y = O
        
    elif x == 'P':
        y = P
        
    elif x == 'R':
        y = R
        
    elif x == 'S':
        y = S
        
    elif x == 'T':
        y = T
        
    elif x == 'U':
        y = U
        
    elif x == 'V':
        y = V
     
    elif x == 'W':
        y = W
        
    else:
        y = blank
        
    return y
    

for n in formatted_dates:
    id, i1, i2, i3, i4, i5, i6, i7, i8, i9 = n
    
    print(i5)
    
    image_1 = determineL(i1)
    image_2 = determineL(i2)
    image_3 = determineL(i3)
    image_4 = determineN(i4)
    image_5 = determineN(i5)
    image_6 = determineN(i6)
    image_7 = determineL(i7)
    image_8 = determineL(i8)
    image_9 = determineL(i9)


  

    #place images in grid
    grid_image.paste(image_1, (153, 115))
    grid_image.paste(image_2, (731, 115))
    grid_image.paste(image_3, (1308, 115))
    grid_image.paste(image_4, (153, 735))
    grid_image.paste(image_5, (731, 735))
    grid_image.paste(image_6, (1308, 735))
    grid_image.paste(image_7, (153, 1357))
    grid_image.paste(image_8, (731, 1357))
    grid_image.paste(image_9, (1308, 1357))
    
    name = "day" + id + ".png"

    grid_image.save(name)

    # folder_path = '/folder'
    # if not os.path.exists(folder_path):
    #     os.makedirs(folder_path)
    # image_path = os.path.join(folder_path, 'grid.png')
    # grid_image.save(image_path)
    #varrible that has day # in it
    #export into folder
