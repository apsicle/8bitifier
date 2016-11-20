from scipy.misc import imread
from scipy.misc import imsave
import numpy as np
import bisect
import nes

#sample usage ---- x = imread("food.jpg") => x = ndarray(height(x), width(y)), 256 val RGB elements

nes_file = file("nes_palette.txt")
text = nes_file.readlines()
data = [line.rstrip('\n') for line in text]
data = [line.split(",") for line in data]
data = [map(int, line) for line in data]

keys = np.array(data)
distance = np.sqrt(keys * keys)
distance = [sum(pixelval) for pixelval in distance]
X = data
Y = map(int, distance)

data_by_distance = [x for (y,x) in sorted(zip(Y,X))]
distance = sorted(Y)



def bitify(filename, rate = 10, method = "recolor"):
    array = imread(filename)
    if method == "recolor":
        recolored = recolor(array, rate)
    elif method == "colorize":
        recolored = colorize(array)
    name = filename.split(".")
    outstring = name[0] + method + "." + name[1]
    imsave(outstring, recolored)

palette = list(range(0,257,  8))

nes_palette = data_by_distance
palette = [list(range(0,257,  8)), list(range(0,257,  8)), list(range(0,257,  8))]
palette1 = []
palette1.append([x[0] for x in nes_palette])
palette1.append([x[1] for x in nes_palette])
palette1.append([x[2] for x in nes_palette])

#distance is imported

def colorize(array, method = "range", palette1 = palette):
    if method == "range":
        xdim = array.shape[1]
        ydim = array.shape[0]
        count = 0
        for i in np.arange(ydim):
            for j in np.arange(xdim):
                print count
                count += 1
                r = array[i][j][0]
                g = array[i][j][1]
                b = array[i][j][2]

                #This section rounds the RGB elements to the nearest color in 'palette'
                if(r >= palette1[0][-1]):
                   pass
                else:
                    r_1 = bisect.bisect_right(palette1[0], r)
                    array[i][j][0] = max(palette1[0][r_1], palette1[0][r_1-1])

                if(g >= palette1[1][-1]):
                   pass
                else:
                    g_1 = bisect.bisect_right(palette1[1], g)
                    array[i][j][1] = max(palette1[1][g_1], palette1[1][g_1-1])

                if(b >= palette1[2][-1]):
                   pass
                else:
                    print i,j

                    b_1 = bisect.bisect_right(palette1[2], b)
                    print b_1
                    array[i][j][2] = max(palette1[2][b_1], palette1[2][b_1-1])
        return array
    if method == "nes":
        count = 0
        xdim = array.shape[1]
        ydim = array.shape[0]
        for i in np.arange(ydim):
            for j in np.arange(xdim):
                print count
                count += 1

                pixel_distance = np.sqrt(array[i][j][0]**2 + array[i][j][1]**2 + array[i][j][2]**2)
                if pixel_distance >= distance[-1]:
                    array[i][j] = nes_palette[-1]
                else:
                    tester = bisect.bisect_right(distance, pixel_distance)
                    if distance[tester] - pixel_distance > pixel_distance - distance[tester-1]:
                        array[i][j] = nes_palette[tester]
                    else:
                        array[i][j] = nes_palette[tester-1]
        return array


def avgBlock(x,y, array, size):
    #assuming block of g h i
    #                  d e f
    #                  a b c
    #where x, y are the coordinates of pixel a, avgBlock(0,0, array, size = 3) will
    #produce a pixel with the averages of the 3x3 pixel shown above.
    avg_pixel = [0,0,0]
    for i in np.arange(size):
        for j in np.arange(size):
            a = array[x + i][y + j]
            avg_pixel += a
    avg_pixel = avg_pixel / (size*size)
    return avg_pixel.astype(int)

def fillBlock(x,y, array_to_fill, pixel_to_use, size):
    for i in np.arange(size):
        for j in np.arange(size):
            array_to_fill[x+i][y+j] = pixel_to_use

def recolor(array, rate):
    xdim = array.shape[1]
    ydim = array.shape[0]
    for i in np.arange(ydim / rate):
        for j in np.arange(xdim / rate):
            pixel = avgBlock(i*rate, j*rate, array, rate)
            fillBlock(i*rate, j*rate, array, pixel, rate)
    return array

def saturate(array, exponent):
    xdim = array.shape[1]
    ydim = array.shape[0]
    for i in np.arange(ydim):
        for j in np.arange(xdim):
            array[i][j][0] = array[i][j][0]**exponent
            array[i][j][1] = array[i][j][1]**exponent
            array[i][j][2] = array[i][j][2]**exponent
    return array

cm = imread("cm.jpg")
def reset(array = cm):
    cm = imread("cm.jpg")


recolored = recolor("food.jpg", 20)
imsave("testrecolor.png", recolored)

def compress(array,rate):
    xdim = array.shape[1]
    ydim = array.shape[0]
    compressed = np.empty(((array.shape[0]/rate)+1, (array.shape[1]/rate)+1, array.shape[2]))
    for i in np.arange(ydim / rate):
        for j in np.arange(xdim / rate):
            compressed[i][j] = avgBlock(i*rate,j*rate,array,rate)
    return compressed

compressed = compress(food, 5)
imsave("testcompressed.png", compressed)



