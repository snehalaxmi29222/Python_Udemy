import numpy as np

array1 = np.array([1,2,3,4])
array2 = np.array([10,20,30,40])

result_add = array1 + array2
result_multi = array1 * array2

comparison = array1 > array2

array3 = np.array([1,2,3,4,5])
scaler = 5
result_broadcast = array3 + scaler

print(result_add)
print(result_multi)
print(comparison)
print("Broadcasting result:", result_broadcast)
