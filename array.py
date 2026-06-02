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

# a = ["python","java","c++","javascript"]
# k = np.random.choice(a,2)    # it will select 2 random elements from the list a
# print(k)

#-------------Broadcasting Operator------------
# a = np.zeros((2,3))+6
# print(a)

# a = np.zeros((2,3),dtype=int)+6
# print(a)

# a = np.zeros((2,3),dtype=int)-6
# print(a)

'''[[-6 -6 -6]
 [-6 -6 -6]]

'''
# a = np.ones((3,4),dtype=int)*5
# print(a)
'''output {
[[5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]]
}'''

'''random rand'''
# a = np.random.rand(10)
# print(a)


'''linspace'''  # it give equal values or distance
# k = np.linspace(1,10,4,retstep=True,dtype=int)
# print(k)


''' if we want to insert the value in array then we use insert function'''
# k = np.array([1,2,54,54,23,67,5])
# print(k)
# print(np.insert(k,3,34))  #(arrayname,index,value) with this we can insert with position
# print(np.append(k,400)) # with the help of append we can insert the value in last 
# print(np.delete(k,2))  #with the help of delete module we can delete with indexing number 

''''to find the row and column in array '''
# k = [[1,2,3],[23,24,1],[4,3,6]]
# j = np.array(k)
# print(j)
# print("dimesion",np.ndim(j))
# print("rows and column",j.shape)
# print("size",j.size)

''' to convert row into column and column into row'''
# k = [[1,2,3],[23,24,1],[4,3,6]]
# j = np.array(k)
# print(np.transpose(j))


''' to add the two array if they are 1d and 2d'''
# a1 = [1,2,4,5,3]
# a2 = [3,2,6,4,3]
# d1 = np.array(a1)
# d2 = np.array(a2)
# print(np.add(d1,d2))

'if we add 2d so we should convert it into 2d with {reshape}'
# s1 = d1.reshape(1,5)
# s2 = d2.reshape(1,5)
# print(np.add(s1,s2))

# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# print(np.delete(a,1,axis=0))  # it will delete the row with index 1
# print(np.delete(a,1,axis=1))  # it will delete the column with index 1

# a = np.array([10,20,30,40,50])
# 30 convert into 300
# a[2] = 300
# print(a)

# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# a[1,1] = 400
# print(a)

# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# for i in np.nditer(a):  # it will iterate through each element of the array a and print it
#     print(i)

#normal for loop -> it will iterate through each row of the array a and print it

# for i,v in np.ndenumerate(a):  # it will iterate through each element of the array a and print its index and value
#     print(i,v)

# maths & stats functions of numpy
'''a = np.array([1,2,3,4,5])
b = np.array([10,20,30,40,50])
print(np.add(a,b))  # it will add the two arrays element wise
print(np.subtract(a,b))  # it will subtract the two arrays element wise
print(np.multiply(a,b))  # it will multiply the two arrays element wise
print(np.divide(a,b))  # it will divide the two arrays element wise
print(np.square(a))  # it will return the square of each element in the array a
'''
# a = np.array([-1,-2,3,4,5])
# print(np.abs(a)) # it will convert the negative values into positive values and return the absolute value of each element in the array 

# a = np.array([1,2,3,4,5])
# print(a.max())  # it will return the maximum value in the array a
# print(a.min())  # it will return the minimum value in the array a
# print(a.mean())  # it will return the mean value of the array a
# print(a.std())  # it will return the standard deviation of the array a

# a  = np.array([1,2,3,4,5,6])
# print(np.split(a,3))    # it will split the array a into 3 equal parts and return a list of arrays

''' if we want to access the first array from the list of arrays then we can use indexing'''
# a = np.array([1,2,3,4,5,6])
# b = np.split(a,3)
# print(b)
# x = b[0]  # it will return the first array from the list of arrays b
# print(x)

# t1 = np.array([1,2,3,4,5])
# t2 = np.array([6,7,8,9,10])
# k = np.hstack((t1,t2))  # it will stack the two arrays horizontally and return a new array
# print(k)
# v = np.vstack((t1,t2))  # it will stack the two arrays vertically and return a new array
# print(v)


# nomral dot
# a1 = np.array([1,2,3])
# a2 = np.array([4,5,6])
# print(np.dot(a1,a2))     #it will return multiply (1*4 + 2*5 + 3*6) and return the dot product of the two arrays a1 and a2
# it is also called broadcasting bcz it multiplies the corresponding elements of the two arrays and returns the sum of the products

# Cross Product
# a1 = np.array([1,2,3])
# a2 = np.array([4,5,6])
# print(np.cross(a1,a2))  # it will return the cross product of the two arrays a1 and a2
# # it is also called vector product bcz it returns a vector that is perpendicular to both a1 and a2 and has a magnitude equal to the area of the parallelogram that the vectors span 

#slice
# a = np.array([1,2,3,4,5,6])
# print(a[0:5:1 ])   

a = np.array([[1,2,3],[4,5,6],[7,8,9],[2,3,8]])
print(a[2:4:1,1:3:1])  