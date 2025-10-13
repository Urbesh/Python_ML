# Convert an array of floats [1.1, 2.2, 3.3] into integers
import numpy as np
arr_float=np.array([1.1, 2.2, 3.3])
print(arr_float)
print(f"Data Type: {arr_float.dtype}")
arr_int=arr_float.astype(np.int32)
print(arr_int)
print(f"Changed Datatype: {arr_int.dtype}")