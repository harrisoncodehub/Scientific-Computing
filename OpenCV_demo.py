import cv2
import numpy as np

#read in an image in opencv
image = cv2.imread("img/cones1.png")

# get size 
numRows = image.shape[0] # height of the image
numCols = image.shape[1] # width of the image
print("Size:", numRows, numCols)

# create an empty grid - size1: rows, size2: cols, 3 color channels 
size1 = 500 
size2 = 500
emptyIm = np.zeros( (size1, size2, 3), np.float32)   

# iterate through the pixels and change the colors
for i in range(numRows):    # height of the image, y coordinates
    for j in range(numCols): # width of the image, x coordinates

        #image[i][j][0]: blue
        #image[i][j][1]: green
        #image[i][j][2]: red
##
##        # only keep green channel
##        image[i][j][0] = 0
##        image[i][j][2] = 0

##        # copy blue image into empty image
##        emptyIm[i][j][0] = image[i][j][0] 


        avgInt = (float(image[i][j][0]) + float(image[i][j][1]) + float(image[i][j][2])) /3.0 
        #copy the blue channel into the empty image
        emptyIm[i][j][0] = image[i][j][0]

        #copy the green channel into the empty image
        emptyIm[i][j][0] = image[i][j][1]

        #copy the red channel into the empty image
        emptyIm[i][j][0] = image[i][j][2]

        # image[i][j][0]: blue channel at location at row i, col
        # image[i][j][1]: green channel at location at row i, col j
        # image[i][j][2]: red channel at location at row i, col j


###Displaying an image 
##cv2.imshow("Displaying an image", image)
        
#Displaying an empty image
cv2.imshow("Displaying an image", emptyIm/255.0)

cv2.waitKey(0) # not going to proceed until you hit 'enter'
cv2.destroyAllWindows() # closes all windows opened with 'imshow'

# save an image
cv2.imwrite("savedImage.png", emptyIm/255.0)
print("Saved") 

