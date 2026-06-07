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
# a = np.zeros((2,3),dtype=bool)+True
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

# l = np.linspace(1,10,2,retstep=True,dtype=int)
# print(l)


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

# a = np.array([[1,2,3],[4,5,6],[7,8,9],[2,3,8]])
# print(a[2:4:1,1:3:1])  

# a1 = np.array([1,2,3,4,5])
# a2 = np.array([10,20,30,40,50])
# k= np.concatenate((a1,a2))  # it merge two arrays
# print(k)
# k1 = np.hstack((a1,a2))  # it work same as concatenate. it add column wise
# print(k1)
# k2 = np.vstack((a1,a2))   # it convert 1d into 2d array . it add row
# print(k2)

# a1 = np.array([[1,2],[3,4]])
# a2 = np.array([[10,20],[30,40]])
# k1 = np.hstack((a1,a2)) # it add according to column wise
# k2 = np.vstack((a1,a2))  # it add according to Row wise
# print(k1)
# print(k2)

# flatten => it convert multiple dimesion into 1d array. it copy the array
# ravle => it share the memory address and also change the original values.

# a = np.array([[1,2,3],[2,3,2]])
# print(a.ndim)
# x = a.flatten()   #----> it convert in 1d array /  there is no relationship in old and new varible created by flatten
# print(x)
# print(x.ndim)
# x = np.append(x,10)   # --> with the help of append we can add any value but we shold give in which we want to add the value
# print(x)

# a = np.array([[1,2,3,4,5]])
# print(a)
# x = a.ravel()  # it share the memory address and the change the original copy
# print(x)
# x[1] = 200
# print(x)    # [  1 200   3   4   5]
# print(a)    # [[  1 200   3   4   5]]  -> in this original array alos changed


# the major differnce is it doesn't convert into 1d array
# copy ----> flatten
# view ----> ravel      

# copy 
# a = np.array([[1,2,3,4,5]])
# print(a)
# x = a.copy()   # it copy but doesn't convert into 1d array
# print(x)

# views
# a = np.array([[1,2,3,4,5]])
# print(a)
# x = a.view()  # it share the memory address and the change the original copy
# print(x)
# x[0] = 200
# print(x)    # [  1 200   3   4   5]
# print(a)

#Matrix Multiplication -> it require minimun two and 2-d arrays. it is use for matrix
# x1 = np.array([[1,2],[3,4]])
# x2 = np.array([[6,2],[7,4]])
# print(x1@x2)


#Searching --> it return on index base
# a = np.array([10,20,3,5,54,23])
# l = np.where(a>30)
# print(l) 

# a = np.array([10,20,3,5,54,23])
# l = np.where(a>5)
# print(l) 
#output -> (array([0, 1, 4, 5]),)

# a = np.array([10,20,3,5,54,23])
# l = np.where(a>5)
# print(a[l]) 
#output -> (array([10 20 54 23]),)

# a = np.array([10,20,3,5,54,23])
# l = np.where(a%2==0)   #it return all even numbers
# print(a[l])

# a = np.array([10,20,3,5,54,23])
# l = np.where(a%2==0,1,0)   #it return all even numbers
# print(l)

# x = np.array([1,2,3,5,6])
# y = np.array([3,3,22,3,4])
# print(np.where(x>y,x,y))

# a = np.array([1,2,3,4,5])
# b  = np.array([10,20,30,40,50])
# c = a+b
# print(c)
# np.save("myfile",c) #it is use to create the file
# np.load("myfile.npy")  # it is use to show the data 
# np.savetxt("boss2.txt",c,fmt="%d",header="welcome to my file",footer="Done")
# np.loadtxt("boss2.txt")

# a = np.array([1,29,34,23,50])
# b = np.array([23,12,43,34,23])
# c = np.where(a>b,a,b)
# np.savetxt('boss2.txt',b)
# np.loadtxt("boss2.txt")

# n = np.array([2,3,6,7,3,8,9,10])
# ar = np.where(n%2==1,-1)
# print(ar)

# a = np.array([1,20,3,121,1,3,2,3])
# print(np.unique(a)) #it will return the unique value and sort it in ascending order

# a = np.array([0,0,1,2,3,0,0])
# print(np.trim_zeros(a))  #it will remove the zeroes from first and last
# print(np.trim_zeros(a,trim='f'))  #it will rremove the front zeros
# print(np.trim_zeros(a,trim='b'))  #it will rremove the back zeros

# a = np.array([10,20,30,40,50])
# b = np.array([10,2,3,50,40])
# print(np.intersect1d(a,b))  #return common values form both array
# print(np.union1d(a,b))      #return all values from both array except duplicated values 
# print(np.setxor1d(a,b))     # return the values that are not common

# v1 = np.array([1,2,3,4,5])
# v2 = np.array([20,38,43,56,45])
# v3 = np.array([200,308,403,576,485])
# f = list(zip(v1,v2,v3))  # we can also convert this into a list with the help of zip
# print(f)
# for i in zip(v1,v2,v3):  # this function is used to iterate multiple arrays
#     print(np.sum(i))

#store a null value in list
# a = [1,5,6,None] 
# a = [1,5,6,np.nan]  # np.nan is a null value in numpy. In core python it is None value
# k = np.array(a)
# print(np.isnan())

# a = np.array([19,0,12,3,0,34,0])
# print(a)
# print(np.count_nonzero(a))  # it will count the non-zero in array
# print(np.nonzero(a)) # it will return the index of nonzero

# a = np.array([1,2,3,4,6,7,4,3,3,]).reshape(3,3)
# b = np.array([1,2,3,4,6,7,4,3,3]).reshape(3,3)

# print(a@b)

# remove the duplicate values from the array
# arr = np.array([1,2,3,4,5,6,7,8,9,1,2,3])
# print(np.unique(arr))


# Create a 10×10 multiplication table using NumPy.
a = np.array(range(1,11)).reshape(10,1)  # it will create a column vector
b = np.array(range(1,11)).reshape(1,10)  # it will create a row vector
multiplication_table = a @ b  # it will perform matrix multiplication and return the multiplication table