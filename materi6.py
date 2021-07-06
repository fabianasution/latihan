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

a1 = [1,2,3,4,5]
b1 = ["a","b","c","d","e"]

# zip sytax menggabungkan suatu list

zip_a = list(zip(a1, b1))

print(zip_a)

zip_b = tuple(zip(a1, b1))

print(zip_b)

zip_c = dict(zip(a1, b1))

print(zip_c)