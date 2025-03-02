import numpy as np

array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
array_3d = np.array([[[10,20],[30,40]],[[50,60],[70,80]],[[90,100],[110,120]]])

#print(array_2d)
#print(array_3d)

#element_2d = array_2d[1,2]
#element_3d = array_3d[1,0,1]

slice_2d = array_2d[:,1:3]
slice_3d = array_3d[1, :, :]

#print(element_2d)
#print(element_3d)

print(slice_2d)
print(slice_3d)
