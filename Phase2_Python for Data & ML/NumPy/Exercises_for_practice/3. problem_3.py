#Find the memory size of a NumPy array with 1 million elements

import sys
import numpy as np
list_data=list(range(1_000_000))
arr1=np.array(list_data)
print(f"Space used by list: {sys.getsizeof(list_data)*len(list_data)} bytes")
print(f"Space used by NumPy arrays: {arr1.nbytes} bytes")