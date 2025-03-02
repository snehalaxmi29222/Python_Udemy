import numpy as np

array = np.array([[1,2,3], [4,5,6], [7,8,9]])

np.savetxt('array.txt', array, delimeter=',')
np.save('array.npy', array)
print("Array saved to 'array.tnpy'")

loaded_array = np.loadtxt('array.npy', delimeter=',')
print(loaded_array)

loaded_binary_array = np.load('array.npy')
print(loaded_binary_array)
