# list comprehension

# syntax nya    -- list_baru = [expression] --

angka = [2,4,6,8,10]

angka2lambda = list(map(lambda x: x**2, angka)) 

print(angka2lambda)

angka2list = [i ** 2 for i in angka]

print(angka2list)

# mencari irisan

a = [2,3,4,5,6,7,8]
b = [5,6,7,8,8,9]

irisan = [i for i in a for j in b if i == j]

print(irisan)

