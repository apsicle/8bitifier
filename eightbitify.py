from scipy.misc import imread
from scipy.misc import imsave
import numpy as np
import bisect
import nes

#sample usage ---- x = imread("food.jpg") => x = ndarray(height(x), width(y)), 256 val RGB elements
def go(speed = np.e, img = "cm.jpg", order = "01"):
    '''ordering: 0 = recolor, 1 = hue.'''

    array = imread(img).astype(int)
    recolor(array)
    hue(array, speed)


    #160 across is really nice (ie. xdim / rate = 160.
    outstring = img.split(".")
    outstring = outstring[0] + "hue%d"%speed + "recolorauto" + ".jpg"
    imsave(outstring, array)

def sig(x, speed = np.e):
    return 256/(1+speed**(-(x-128)/32.0))

def sigmoid(x):
    return 1/(1+np.exp(-x))

#distance is imported
def hue(array, speed):
    palette = [list(range(0,257,  32)), list(range(0,257,  32)), list(range(0,257,  32))]
    palette[2][0] = 1
    xdim = array.shape[1]
    ydim = array.shape[0]
    count = 0
    for i in np.arange(ydim):
        for j in np.arange(xdim):

            count += 1
            r = sig(array[i][j][0], speed)
            g = sig(array[i][j][1], speed)
            b = sig(array[i][j][2], speed)
            if i == 85 and j == 114:
                if(r >= palette[0][-1]):
                    pass
                else:
                    r_1 = bisect.bisect_right(palette[0], r)
                    array[i][j][0] = max(palette[0][r_1], palette[0][r_1-1])

                if(g >= palette[1][-1]):
                    pass
                else:
                    g_1 = bisect.bisect_right(palette[1], g)
                    array[i][j][1] = max(palette[1][g_1], palette[1][g_1-1])

                if(b >= palette[2][-1]):
                   pass
                else:
                    b_1 = bisect.bisect_right(palette[2], b)
                    x = max(palette[2][b_1], palette[2][b_1-1])
                    print "%d <-this is to be put into array"%x
                    print "%d <- this is the current array value"%array[i][j][2]
                    array[i][j][2] = x #assignment
                    print "%d <- this is array after assignment"%array[i][j][2]
            else:
                if(r >= palette[0][-1]):
                    pass
                else:
                    r_1 = bisect.bisect_right(palette[0], r)
                    array[i][j][0] = max(palette[0][r_1], palette[0][r_1-1])

                if(g >= palette[1][-1]):
                    pass
                else:
                    g_1 = bisect.bisect_right(palette[1], g)
                    array[i][j][1] = max(palette[1][g_1], palette[1][g_1-1])

                if(b >= palette[2][-1]):
                   pass
                else:
                    b_1 = bisect.bisect_right(palette[2], b)
                    array[i][j][2] = max(palette[2][b_1], palette[2][b_1 - 1])


            #Want a function that is zero-centered with positive slope >1 increasing with larger magnitude

def avgBlock(y,x, array, ratex, ratey):
    #assuming block of g h i
    #                  d e f
    #                  a b c
    #where x, y are the coordinates of pixel a, avgBlock(0,0, array, size = 3) will
    #produce a pixel with the averages of the 3x3 pixel shown above.
    avg_pixel = [0,0,0]
    for i in np.arange(ratey):#y
        for j in np.arange(ratex):
            a = array[y + i][x + j]
            avg_pixel += a
    avg_pixel = avg_pixel / (ratey*ratex)
    return avg_pixel.astype(int)

def fillBlock(y,x, array_to_fill, pixel_to_use, ratex, ratey):
    for i in np.arange(ratey):
        for j in np.arange(ratex):
            array_to_fill[y+i][x+j] = pixel_to_use

def recolor(array):
    #This function is not inplace ie. doesn't modify the original array
    xdim = array.shape[1]
    ratex = xdim / 160
    if((ratex * 160) - xdim > ((ratex+1) * 160) - xdim):
        ratex = ratex + 1
    ydim = array.shape[0]
    ratey = ydim / 128
    if((ratey * 128) - ydim > ((ratey+1) * 160) - ydim):
        ratey = ratey + 1
    i = 0
    while((i+1) * ratey < ydim):
        j = 0
        print i, j, ratex, ratey, xdim, ydim
        while((j+1) * ratex < xdim):
            print i, j, ratex, ratey, xdim, ydim
            pixel = avgBlock(i*ratey, j*ratex, array, ratex, ratey)
            fillBlock(i*ratey, j*ratex, array, pixel, ratex, ratey)
            j += 1
        i += 1
    return array

def compress(array,rate):
    xdim = array.shape[1]
    ydim = array.shape[0]
    compressed = np.empty(((array.shape[0]/rate)+1, (array.shape[1]/rate)+1, array.shape[2]))
    for i in np.arange(ydim / rate):
        for j in np.arange(xdim / rate):
            compressed[i][j] = avgBlock(i*rate,j*rate,array,rate)
    return compressed



