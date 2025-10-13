#Use fancy indexing to extract even numbers from [1, 2, 3, 4, 5, 6]
import numpy as np
arr=np.array([1,2,3,4,5,6])
even=arr%2==0
print(arr[even])