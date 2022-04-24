import numpy as np

ar = np.arange(4)
ar_from_list = np.array([1, 2, 3, 4], dtype=np.int8) # by deafult dtype is int32, dtype is optional

print(type(ar_from_list[0]))

print(ar)
print(type(ar))