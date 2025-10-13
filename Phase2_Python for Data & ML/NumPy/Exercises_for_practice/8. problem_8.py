#Use boolean masking to filter numbers greater than 50 in an array.
import numpy as np
arr=np.array([list(range(1, 101, 5))])
mask=arr>50
print(arr[mask])