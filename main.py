from operator import neg
from os import nice
import cv2 as cv
import numpy as np
import struct
import matplotlib.pyplot as plt


img_orig = cv.imread('cropped.png')

#for i in range(i_range):
    #x-axis loop
#    for j in range(j_range):
        #Store each RGB value
#        R, G, B = img[i, j]
#        print("RGB:",[R,G,B])

img = cv.cvtColor(img_orig, cv.COLOR_BGR2RGB) #Contents of img:[y coordinate,x coordinate, [R, G, B]]
cv.imshow('edges',img_orig)
cv.waitKey(0)

#Array for storing coordinates
#graph_coordinate = [[0 for i in range(3)] for j in range(i_range * j_range)]

#Get the number of elements on the x-axis and y-axis
i_range = img.shape[0]
j_range = img.shape[1]
graph_coordinate = []
x_list = []
R_range = [60,100]
G_range = [110,160]
B_range = [180,210]
#y-axis loop
for i in range(i_range):
    #x-axis loop
    for j in range(j_range):
        #Store each RGB value
        R, G, B = img[i, j]
#        print("RGB:",[R,G,B])
        #Get only the coordinates that match the graph color
        if (R_range[0] <= R <= R_range[1]) and (G_range[0] <= G <= G_range[1]) and (B_range[0] <= B <= B_range[1]):
#                graph_coordinate.insert(idx,[i, j, img[i, j]])
                graph_coordinate.append([i, j, img[i, j]])
                x_list.append(j)
coordinate = np.asarray(graph_coordinate)
length = len(x_list)
x = []
y = []
for ii in range(length):
    x.append(graph_coordinate[ii][0])
    y.append(graph_coordinate[ii][1])
#Find the y coordinate from the maximum value on the x axis (x coordinate at the end of the graph)
negx = []
negx = [-el for el in x]

data = np.c_[y,negx]
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.title('Interpolated graph function')
plt.plot(y,negx,'*')
#plt.show()


np.savetxt('output.dat', data, delimiter=',')