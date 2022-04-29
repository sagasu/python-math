import numpy as np

ar = np.arange(4)
ar_from_list = np.array([1, 2, 3, 4], dtype=np.int8) # by deafult dtype is int32, dtype is optional

print(type(ar_from_list[0]))

empty_array  = np.zeros((2, 3))
print(empty_array)

array_ones = np.ones((2, 3))
print(array_ones)

print(ar)
print(type(ar))