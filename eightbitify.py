from scipy.misc import imread
from scipy.misc import imsave
import numpy as np
import bisect

#sample usage ---- x = imread("food.jpg") => x = ndarray(height(x), width(y)), 256 val RGB elements

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

def colorize(array):
    xdim = array.shape[1]
    ydim = array.shape[0]
    for i in np.arange(ydim):
        for j in np.arange(xdim):
            r = array[i][j][0]
            g = array[i][j][1]
            b = array[i][j][2]

            #This section rounds the RGB elements to the nearest color in 'palette'
            if(r == 256):
               pass
            else:
                r_1 = bisect.bisect_right(palette, r)
                array[i][j][0] = max(palette[r_1], palette[r_1-1])

            if(g == 256):
               pass
            else:
                g_1 = bisect.bisect_right(palette, g)
                array[i][j][1] = max(palette[g_1], palette[g_1-1])

            if(b == 256):
               pass
            else:
                b_1 = bisect.bisect_right(palette, b)
                array[i][j][2] = max(palette[b_1], palette[b_1-1])
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

recolored = recolor(food, 20)
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



