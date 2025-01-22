import cv2
import numpy as np

SCALER = 2

image = cv2.imread("img/vangogh.jpg")

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
grayscale = np.zeros((n,n,3), np.float32) 

###Create new color image
##coloredIm = np.zeros((n,n,3), np.float32)
##cv2.imshow("Colored Image", coloredIm) 

# iterate over all the pixels in the image
for i in range(1,numRows-1): # height of the image, y coordinates
    for j in range(1,numCols-1): # width of the image, x coordinates
    # convert to grayscale, preserve intensity
        avgInt = 0.082 * float(image[i][j][0]) + 0.609 *float(image[i][j][1]) + 0.309 * float(image[i][j][2])
    ## copy the blue channel into empty image
        grayscale[i][j][0] = avgInt

    ## # copy the green channel into empty image
        grayscale[i][j][1] = avgInt

    ## # copy the green channel into empty image
        grayscale[i][j][2] = avgInt


# Compute starting positions for centering
x_offset = (n - numCols) // 2
y_offset = (n - numRows) // 2

# Iterating through the pixels and copying the colors
for i in range(numRows):  # Loop over image rows
    for j in range(numCols):  # Loop over image columns
        emptyIm[y_offset + i, x_offset + j] = image[i, j]
        grayscale[y_offset + i, x_offset + j] = image[i, j]



# Displaying the image 
cv2.imshow("Displaying the image", image) 

#Displaying empty image and gray scale 
cv2.imshow("Displaying empty image", emptyIm/255.0)
cv2.imshow("Displaying grayscale", grayscale/255.0) 


cv2.waitKey(0)
cv2.destroyAllWindows() 


