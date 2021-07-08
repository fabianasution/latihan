# database = {
#             "senin" : 1,
#             "selasa" : 2,
#             "rabu" : 3,
#             "kamis" : 4,
#             "jumat" : 5,
#             "sabtu" : 6,
#             "minggu" : 7
#         }


# database.update({"wow" : 8})

# print(database)

# database["wow"] = [1,2,3]

# print(database)

# database["wow"].insert(1, 4)

# print(database)

# # kotak berisi 300 bola mengambil 3 bola 

# (1/150) * (1/75)

# import numpy

# import scipy

import mysql.connector
import jupyter
import numpy as np

a = [5, 6, 7, 8, 9, 10]
b = [[1,2,3],[4,5,6],[7,8,9]]

n = np.array(a)
m = np.matrix(b)

print(a)
print(n)
print(m)

print(n[0])

print(m[2,0])

print("=" * 100)

# operasi math basic numpy

c = n + 5 ## setiap elemen di tambah 5 

print(c)

d = n * 3 
e = m * 3
print(d)
print(e) # it apply to all math operator

print("=" * 100)

for i in np.arange(1, 10.5, 0.5): # able to operate float in range
    print(i)

print("=" * 100)
#  liniar Space 

b1 = np.linspace(0, 100, 11)
print(b1)

print("=" * 100)

# NP array sort

x = [2,4,6,3,1,10,9,5,6,7,8]

x1 = np.sort(x)
print(x1)

y = [11, 12, 13, 14, 16, 17, 15]
y1 = np.sort(y)

# menggabungkan array 
xy = np.concatenate((x1, y1))

print(xy)

x2 = np.array([[1, 2], [3, 4]])
y2 = np.array([[5, 6]])

matrixxy = np.concatenate((x2, y2), 0)

print(matrixxy)

print("=" * 100)

# logaritmik space (LOG)

d1 = np.logspace(0, 5, 6)

print(d1)

print("=" * 100)

# dimension
print("Shape of Matrix")
array_example = np.array([[[0, 1, 2, 3, 8],
                           [4, 5, 6, 7, 8]],

                           [[0, 1, 2, 3, 8],                        
                           [4, 5, 6, 7, 8]],

                          [[0 ,1 ,2, 3, 8],
                           [4, 5, 6, 7,8 ]]])


o = array_example.ndim #Dimension
o1 = array_example.size #size
o2 = array_example.shape #Shape 3 = dimension, 2 = row 5 = column

print(o)
print(o1)
print(o2)
print(array_example.dtype)

print("=" * 100)

matf = array_example.astype("float64") # atau bisa di ganti "int64" 64 adalah bit nya 

print(matf)
print("=" * 100)

# NP array random 

randomarray = np.random.rand(2, 4) #Matrix row column
randomarray2 = np.random.rand(3, 2, 4) #Matrix dimension row column

randomarray1 = np.random.randn(3,2,4) #membuat normal distribution antara -3 sampai 3 kebanyankan di -1 sampai 1 

randomarray3 = np.random.rand(10) #membuat random dari 0 - 1


randomarray4 = np.random.randint(0, 10, 11) #integer batasan nya kita yang tentukan, 0 - 10 random, jumlah 10, batas atas exclusive

print(randomarray)
print("=" * 100)

print(randomarray2)
print("=" * 100)

print(randomarray1)
print("=" * 100)

print(randomarray3)
print("=" * 100)

print(randomarray4)
print("=" * 100)


# menggabungkan array 

x2 = np.array([[1, 2]])
y2 = np.array([[5, 6]])

matrixxy = np.concatenate((x2, y2), 0)
print("=" * 100)

print(matrixxy)

print("=" * 100)

# membuat matrix dengan function 

def perkalian(row, column):
    return row * column

f = np.fromfunction(perkalian, (3, 4), dtype=int)

print(f)
print("=" * 100)

def penjumlahan(row, column):
    return row + column

f1 = np.fromfunction(penjumlahan, (3, 4), dtype=int)

print(f1)

print("=" * 100)

# membuat matrix 

z = np.zeros((3,2,4))

print(z)

print("=" * 100)

z1 = np.ones((3,2,4))

print(z1)
print("=" * 100)
print("ini")

print(int(z1[1,0,0]))

print(z1[2,0]) #ini dan bawah sama saja 
print(z1[2][0])
print(z1[:,0,3]) #indexing for all the element in matrix but only the one we prefered 

print("=" * 100)

# matrix identity

u = np.eye(5)

u1 = np.identity(5)

print(u1)
print("=" * 100)

# operational math 

a10 = [5, 6, 7, 8, 9, 10]
a11 = [5, 6, 7, 8, 9, 10]

anum = np.array(a10)
bnum = np.array(a11)

hasillist = a10 + a11

hasilnum = anum + bnum #bisa menggunakan operator lain juga

print(hasillist)
print(hasilnum)

print("=" * 100)

array_example2 = np.array([[0, 1, 2, 3, 8],
                           [4, 5, 6, 7, 8]])

array_example3 = np.array([[0, 1, 2, 3, 8],
                           [4, 5, 6, 7, 8]])

hasil = array_example2 * array_example3
print(hasil)

print("=" * 100)

# row reversed of transpose matrix 
# column reversed of transpose matrix 
# 


# update an array 

array_example2[0,0:5] = 50

print(array_example2)

print("=" * 100)

partf = array_example2[0,0 :5]
partf[:] = 13

print(partf)

print(array_example2)

print("=" * 100)

# to copy the index

f2 = array_example2.copy()
f2[0,0:5] = 99

print(f2)

# print which array we want in a matrix
pot = array_example2[0][[3,2,1]]

print(pot)
print("=" * 100)

# conditional slicing

print(array_example2 > 10)

condi = array_example2 > 10

print(array_example2[condi])

# perkalian dot matrix / DOT product

a10 = np.array( [
     [2,4],
     [5,7]   
] )

b10 = np.array([
     [4,3],
     [3,2]   
])

dp = np.dot(a10,b10)

print(dp)



dp1 = np.dot(b10,a10)
print(dp1)

print("=" * 100)
hasil = a10 * b10

print(hasil)

print("=" * 100)

b11 = np.array([
     [5,2,3],
     [1,4,6]   
])


opsi1 = np.flip(b11,0) #Membalik ROW
opsi2 = np.flip(b11,1) #Membalik Column

print(opsi1)
print(opsi2)

print("=" * 100)

b11transpose = np.transpose(b11) #transpose matrix

print(b11transpose)
print("=" * 100)

# flattening matrix 

flat = np.ravel(a10)

print(flat)
print("=" * 100)

# reshaping 

print(b11.reshape(3,2))

print("=" * 100)


# inverse matrix

b100 = np.linalg.inv(b10) #inverse matrix

print(b100)

print("=" * 100)

identity1 = np.dot(b10,b100) # A . A-1 = identity

print(identity1)

print("=" * 100)

# stacking 
stack = np.hstack((a10, b10)) #horizontal
print(stack)

stack = np.hstack((a10, b10)) #vertical
print(stack)


print("=" * 100)

# basic statistic operation
from scipy import stats

list_a = [ 1,2,3,4,5,6,12,34,2,34,56,7,7,96,32,1,2,3,45,6,7,7,88,8]

Blist = np.array(list_a)

Bmean = np.mean(Blist) #MEAN

Bmedia = np.median(Blist) 

Bmode = stats.mode(Blist)

Bq1 = np.percentile(Blist, 25) # Q1
Bq2 = np.percentile(Blist, 75) # Q3

Bmax = np.max(Blist)
Bmin = np.min(Blist)

Bindexmin = np.argmin(Blist) #INDEX
Bindexmax = np.argmax(Blist)

Bstd = np.std(Blist) # Standart deviation from the population

Bsqrt = np.sqrt(Blist)

Bsort = np.sort(Blist)


print(Bmean)
print(Bmedia)
# print(Bmode)

print(Bq1)
print(Bq2)
print(Bmax)
print(Bsort)





















