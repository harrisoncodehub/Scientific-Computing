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
emptyIm_grayScale = np.zeros( (numRows, numCols), np.float32)


# Compute starting positions for centering
x_offset = (n - numCols) // 2
y_offset = (n - numRows) // 2

# Iterating through the pixels and copying the colors
for i in range(numRows):  # Loop over image rows
    for j in range(numCols):  # Loop over image columns
        emptyIm[y_offset + i, x_offset + j] = image[i, j]
        grayscale[y_offset + i, x_offset + j] = grayscale_image[i, j]




# Displaying the image 
cv2.imshow("Displaying original image", image) 

#Displaying empty image and gray scale 
cv2.imshow("Displaying original image in an empty image", emptyIm/255.0)
cv2.imshow("Displaying grayscale of original image in an empty image", grayscale/255.0) 


cv2.waitKey(0)
cv2.destroyAllWindows() 


