import numpy as np

a = np.array([1,2,3], dtype = 'int32')
print(a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

print(a.ndim) # dimension
print(a.shape) # shape
print(b.shape)
print(a.dtype) #get type

print(a.itemsize) #in bytes
print(b.itemsize) #in bytes

a= np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a[1,5]) #get a specific element
print(a[1,:]) #get a specific row

# more fancy [start index: end index : stepsize], or use negative to start from end
print(a[0, 1:6:2])

a[1,5] = 20

print(a)

a[:,2] = [1,2]
print(a)

#3D example
d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d)

print(d[:,1,:])
print(np.full_like(a,4))

print(np.zeros(5))
print(np.ones(5))

#any other number 
print(np.full((2,2),99))

#random numbers
print(np.random.rand(4,2))
print(np.random.random_sample(a.shape))
print(np.random.randint(7, size = (3,3))) #random integer

#identity matraix
print(np.identity(5))

arr = np.array([1,2,3])
r1 = np.repeat(arr,3, axis = 0)
print(r1)

############################################################

output = np.ones((5,5))
print(output)

z= np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:4,1:4] = z #exclusive
print(output)

# b = a means that we are copying the pointer, hence modifying b modifies b
# so we should use b = a.copy()

"""
Arithmetic
a+2
a/2
a*2
a**2
np.sin(a)
a = np.full((2,3),1)
np.matmul(a,b)
np.linalg.det(c) #find determinant
np.min(a)
np.max(a)
np.min(a, axis = 0)

after = before.reshape((2,2,2))
etc.
"""

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

np.vstack([v1,v2,v1,v2])

"""
or do np.hstack

filedata = np.genfromtxt('data,txt', delimiter = ',')
filedata = filedata.astype('int32')
(~(filedata>50) & (filedata<100))


Index multiple entries at the same time
a[[0,1,2,3,4],[1,2,3,4]]
"""