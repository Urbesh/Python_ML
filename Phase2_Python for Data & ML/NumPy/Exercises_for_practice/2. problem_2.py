#Compare the time taken to multiply two Python lists vs. two NumPy arrays.

import numpy as np
import time
#Python list
size = 1_000_000_00 # 
list1=list(range(size))
list2=list(range(size))
start=time.time()
result=[x*y for x,y in zip(list1,list2)]
end=time.time()
print(f"The result is: {result[0:20]}")
print(f"Time taken for python list: {end-start}")

#NumPy arrays
arr1=np.array(list1)
arr2=np.array(list2)
start=time.time()
result=arr1*arr2
end=time.time()
print(f"The result is: {result[0:20]}")
print(f"Time taken for NumPy arrays: {end-start}")