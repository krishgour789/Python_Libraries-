import numpy as np
# p = (1,45,21,43)
# print(type(p))

# a = np.array(p)
# print(a)
# print(type(a))

# lst = [23,26,35,32,64]
# print(type(lst))
# a = np.array(lst)
# print(a)

# a = np.array([12,13,43,233,4])
# print(a)

"with the help of range fucntion"

# a = np.array(range(10))
# print(a)

'with the help of these we can print [1 3 5 7 9] using range function'
'''a = np.array(range(1,10,2))
print(a)
print(a.ndim)  # it is property use to fetch which dimension is this
'''
# Dimesion Reduction
'''a = np.array(range(1,12,2))
b = a.reshape(3,2)
print(b)
print(b.ndim)
'''

# converting into 3 Dimesnions
# a = np.array(range(1,12,2))
# b = a.reshape(2,1,3)
# print(b)
# print(b.ndim)


# zeroes
# zz = np.zeros((3,4))
# print(zz)
# print(zz.ndim)

#arange = it is used to create an array with a range of values
# ar = np.arange(1,10,2)
# print(ar)



# ar = np.arange(1,21,1).reshape(5,4)
# print(ar)

# ar = np.arange(21,1,-1).reshape(5,4,1)
# print(ar)
# print(ar.ndim)

# eye = it is used to create an identity matrix {it is a square matrix with 1's on the diagonal and 0's elsewhere}
# e = np.eye(10)
# print(e)
# print(e.ndim)


'random choice is used to select random elements from a given array'
# k = np.random.choice(20,3)    # it will select 3 random elements from the range of 0 to 19
# print(k)

a = ["python","java","c++","javascript"]
k = np.random.choice(a,2)    # it will select 2 random elements from the list a
print(k)

