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

