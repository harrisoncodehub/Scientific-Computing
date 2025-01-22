import cv2
import numpy as np

#read in an image in opencv
image = cv2.imread("cones1.png")
# if image is in a subfolder, give relative path
# image = cv2.imread("img/cones1.png")

# get size of an image
numRows = image.shape[0] # height of image
numCols = image.shape[0] # width of image
print("Size:", numRows,numCols)

#create a second image, of the same size as the first
emptyIm = np.zeros ( (numRows, numCols, 3), np.float32)

# iterate over all the pixels in the image
for i in range(numRows): # height of the image y coordinates
    for j in range(numCols): # width of the image x coordinates


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




#displaying an image
cv2.imshow("Displaying an image", emptyIm/255.0)

#save an image
cv2.imwrite("savedImg.png", emptyIm/255.0) 

cv2.waitKey(0) # not going to proceed until you hit 'enter'
cv2.destroyAllWindows() # closes all windows opened with 'imshow'
