import numpy as np
array = np.array([10,20,30,40,50,60])
element = array[2] 
slice_of_array = array[1:4]  #slicing
reshaped_array = array.reshape(2,3)  #reshaped
element = array[2]           
print("Original Array:", array)
print("Sliced Array (index 1 to 3):", slice_of_array)
print("Element at index 2:", element)
print("Reshaped Array (2 X 3):", reshaped_array)
