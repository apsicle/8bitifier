import numpy as np

nes_file = file("nes_palette.txt")
text = nes_file.readlines()
data = [line.rstrip('\n') for line in text]
data = [line.split(",") for line in data]
data = [map(int, line) for line in data]

keys = np.array(data)
distance = np.sqrt(keys * keys)
distance = [sum(pixelval) for pixelval in distance]
X = data
Y = distance

data_by_distance = [x for (y,x) in sorted(zip(Y,X))]
distance = sorted(distance)

# Belongs in eightbitify.py but is deprecated

# def colorize(array, method = "range", palette1 = palette):
#     if method == "range":
#         xdim = array.shape[1]
#         ydim = array.shape[0]
#         count = 0
#         for i in np.arange(ydim):
#             for j in np.arange(xdim):
#                 print count
#                 count += 1
#                 r = array[i][j][0]
#                 g = array[i][j][1]
#                 b = array[i][j][2]
#
#                 if(r >= palette1[0][-1]):
#                    pass
#                 else:
#                     r_1 = bisect.bisect_right(palette1[0], r)
#                     array[i][j][0] = max(palette1[0][r_1], palette1[0][r_1-1])
#
#                 if(g >= palette1[1][-1]):
#                    pass
#                 else:
#                     g_1 = bisect.bisect_right(palette1[1], g)
#                     array[i][j][1] = max(palette1[1][g_1], palette1[1][g_1-1])
#
#                 if(b >= palette1[2][-1]):
#                    pass
#                 else:
#                     print i,j
#
#                     b_1 = bisect.bisect_right(palette1[2], b)
#                     print b_1
#                     array[i][j][2] = max(palette1[2][b_1], palette1[2][b_1-1])
#         return array
#                 #This section rounds the RGB elements to the nearest color in 'palette'
#                 if(r >= palette1[0][-1]):
#                    pass
#                 else:
#                     r_1 = bisect.bisect_right(palette1[0], r)
#                     array[i][j][0] = max(palette1[0][r_1], palette1[0][r_1-1])
#
#                 if(g >= palette1[1][-1]):
#                    pass
#                 else:
#                     g_1 = bisect.bisect_right(palette1[1], g)
#                     array[i][j][1] = max(palette1[1][g_1], palette1[1][g_1-1])
#
#                 if(b >= palette1[2][-1]):
#                    pass
#                 else:
#                     print i,j
#
#                     b_1 = bisect.bisect_right(palette1[2], b)
#                     print b_1
#                     array[i][j][2] = max(palette1[2][b_1], palette1[2][b_1-1])
#         return array
#     if method == "nes":
#         count = 0
#         xdim = array.shape[1]
#         ydim = array.shape[0]
#         for i in np.arange(ydim):
#             for j in np.arange(xdim):
#                 print count
#                 count += 1
#
#                 pixel_distance = np.sqrt(array[i][j][0]**2 + array[i][j][1]**2 + array[i][j][2]**2)
#                 if pixel_distance >= distance[-1]:
#                     array[i][j] = nes_palette[-1]
#                 else:
#                     tester = bisect.bisect_right(distance, pixel_distance)
#                     if distance[tester] - pixel_distance > pixel_distance - distance[tester-1]:
#                         array[i][j] = nes_palette[tester]
#                     else:
#                         array[i][j] = nes_palette[tester-1]
#         return array

# Deprecated
#
# nes_file = file("nes_palette.txt")
# text = nes_file.readlines()
# data = [line.rstrip('\n') for line in text]
# data = [line.split(",") for line in data]
# data = [map(int, line) for line in data]
#
# keys = np.array(data)
# distance = np.sqrt(keys * keys)
# distance = [sum(pixelval) for pixelval in distance]
# X = data
# Y = map(int, distance)
#
# data_by_distance = [x for (y,x) in sorted(zip(Y,X))]
# distance = sorted(Y)
#
#
#
# def bitify(filename, rate = 10, method = "recolor"):
#     array = imread(filename)
#     if method == "recolor":
#         recolored = recolor(array, rate)
#     elif method == "colorize":
#         recolored = colorize(array)
#     name = filename.split(".")
#     outstring = name[0] + method + "." + name[1]
#     imsave(outstring, recolored)
