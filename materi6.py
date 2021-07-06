# list comprehension

# syntax nya    -- list_baru = [expression] --

angka = [2,4,6,8,10]

angka2lambda = list(map(lambda x: x**2, angka)) 

print(angka2lambda)

angka2list = [i ** 2 for i in angka]

print(angka2list)

