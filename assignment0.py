# AUTHOR: HARRISON HUBBARD
# DATE: 1/24/25
# COURSE: CSC-340


import cv2
import numpy as np

SCALER = 2

image = cv2.imread("img/vangogh.jpg")
image_grayscale = cv2.imread("img/vangogh.jpg", 0)

# Get size of the image
numRows = image.shape[0] # height 
numCols = image.shape[1] # width 
print("Size: ", numRows, numCols)


#Assigning maximum dimension  
if numRows > numCols:
    maxDim = numRows
elif numCols > numRows:
    maxDim = numCols
else:
    maxDim = numRows

# Create empty image
n = SCALER * maxDim
emptyIm = np.zeros((n,n,3), np.float32)
grayscale = np.zeros((n,n), np.uint8) 

# iterate over all the pixels in the image
for i in range(1,numRows-1): # height of the image, y coordinates
    for j in range(1,numCols-1): # width of the image, x coordinates
        # convert to grayscale, preserve intensity
        avgInt =  0.082 * float(image[i][j][0]) + 0.609 *float(image[i][j][1]) + 0.309 * float(image[i][j][2])
        # copy the blue channel into empty image
        emptyIm[i][j][0] = avgInt

        # copy the green channel into empty image
        emptyIm[i][j][1] = avgInt

        # copy the green channel into empty image
        emptyIm[i][j][2] = avgInt

        
        # invert your RGB values
        avgInt =  0.082 * float(image[i][j][0]) + 0.609 *float(image[i][j][1]) + 0.309 * float(image[i][j][2])
        # copy the blue channel into empty image
        emptyIm[i][j][0] = 255 - image[i][j][0]

        # copy the green channel into empty image
        emptyIm[i][j][1] = 255 - image[i][j][1]

        # copy the green channel into empty image
        emptyIm[i][j][2] = 255 - image[i][j][2]

        # image[i][j][0]: blue channel at location row i, col j
        # image[i][j][1]: green channel at location row i, col j
        # image[i][j][2]: red channel at location row i, col j
    
        emptyIm[i][j]=abs(float(image_grayscale[i+1][j])-float(image_grayscale[i-1][j]))
        

# Compute starting positions for centering
x_offset = (n - numCols) // 2
y_offset = (n - numRows) // 2

# Iterating through the pixels and copying the colors
for i in range(numRows):  # Loop over image rows
    for j in range(numCols):  # Loop over image columns
        emptyIm[y_offset + i, x_offset + j] = image[i, j]
        grayscale[y_offset + i, x_offset + j] = image_grayscale[i, j]




# Displaying the image 
cv2.imshow("Displaying original image", image) 

#Displaying empty image and gray scale 
cv2.imshow("Displaying original image in an empty image", emptyIm/255.0)
cv2.imshow("Displaying grayscale of original image in an empty image", grayscale/255.0) 

cv2.imwrite("savedImg_gradY.jpg", emptyIm)
cv2.imwrite("savedImg_vangogh.jpg", image)
cv2.imwrite("savedImg_rgb.jpg", grayscale)

cv2.waitKey(0)
cv2.destroyAllWindows() 


