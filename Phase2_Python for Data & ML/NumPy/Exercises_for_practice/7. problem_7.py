#Reshape a 1D array of size 9 into a 3×3 matrix
import numpy as np
arr = np.array([8,4,5,3,9,7,6,1,0])
reshaped=arr.reshape((3,3))
print(reshaped)