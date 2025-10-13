#Create a 3x3 array filled with random numbers and print its shape

import numpy as np
my_array=np.random.randint(0,10, size=(3,3))
print(my_array)
print(f"Shape: {my_array.shape}")