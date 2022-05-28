from operator import neg
from os import nice
import cv2 as cv
import numpy as np
import sys
import struct
import matplotlib.pyplot as plt


def img2dat(file,frameCounter):
    img_orig = cv.imread(file)
    img_cropped = img_orig[250:420,110:472]
#    cv.imshow('crop',img_cropped)
#    cv.waitKey(0)
#    img_orig = cv.imread('cropped.png')
    img = cv.cvtColor(img_cropped, cv.COLOR_BGR2RGB) #Contents of img:[y coordinate,x coordinate, [R, G, B]]
#    image = cv.cvtColor(img_cropped, cv.COLOR_BGR2HLS) #Contents of img:[y coordinate,x coordinate, [R, G, B]]
#    lower = np.uint8([0, 200, 0])
#    upper = np.uint8([255, 255, 255])
#    white_mask = cv.inRange(image, lower, upper)
    # yellow color mask
#    lower = np.uint8([150,110,110])
#    upper = np.uint8([210,180,160])
#    yellow_mask = cv.inRange(image, lower, upper)
    # combine the mask
#    mask = cv.bitwise_or(yellow_mask, white_mask)
#    cv.imshow("mask",mask) 
#    cv.imshow('edges',img)
#    cv.waitKey(0)
    #Array for storing coordinates
    #graph_coordinate = [[0 for i in range(3)] for j in range(i_range * j_range)]
    #Get the number of elements on the x-axis and y-axis
    i_range = img.shape[0]
    j_range = img.shape[1]
    graph_coordinate = []
    x_list = []
    R_range = [150,210]
    G_range = [110,180]
    B_range = [110,160]
    #y-axis loop
    for i in range(i_range):
        #x-axis loop
        for j in range(j_range):
            #Store each RGB value
            R, G, B = img[i, j]
            #Get only the coordinates that match the graph color
            if (R_range[0] <= R <= R_range[1]) and (G_range[0] <= G <= G_range[1]) and (B_range[0] <= B <= B_range[1]):
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
    plt.show()
    name  = '__dat_out__//output_'+str(frameCounter)+'.dat'
    np.savetxt(name, data, delimiter=',')

if __name__ == '__main__':
#    inputFile = sys.argv[1]
 #   frameCounter = sys.argv[2]
    inputFile = "__tmp_img__//frame_2.png"
    frameCounter = "1"
    print(inputFile)
    img2dat(inputFile,frameCounter)