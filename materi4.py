# import sys 

# def rumus(input1):
#     a = 7 
#     hasil = input1 + 2 + a
    
#     return(hasil)

# print(rumus(2))

# a = 10

# print(a)

# print(rumus(a))

# def kuadrat(a):
#     x = a ** 2
#     return x

# print("="*50)

# bubur = "banteng banget"
# x = list()

# symbol = "!@$%^&*"
# bule = bubur.index("a")

# test1 = bubur[0].isalpha()
# test2 = bubur[0].isnumeric()


# if test1 == False or test2 == False :
#     print("false")
#     # sys.exit()

# print(bubur)


# test2 = len(bubur)
# print(test2)

# print(bule)
# print(type(bule))
    
# bubur1 = bubur.split(" ")
# print(bubur1)
# print(bubur1[0])

# my_string = "Where's Waldo?"
# my_string.find("Waldo")

# print(my_string.find("waldo"))

#fungsi Lamda 
# fungsi yang biasa di pakai sekali
# fungsi yg sifat nya khusus
# tidak bernama 
# memiliki ukuran kecil 
# hanya memiliki 1 fungsi atau 1 ekspresion
# tidak ada return value


hasil12 = lambda x, y: x * y

print(hasil12(4, 5))

print("="*50)


hasil5 = lambda x: "angka genap" if x%2==0 else "angka ganjil"


print(hasil5(4))

pangkat3 = lambda x: x**3

print("="*50)

a = [5, 8, 15, 10]

# MAP Function

hasilmap = list(map(pangkat3, a))

print(hasilmap)

kali = lambda x,y: x * y

a1 = [25,15,10]
b1 = [10,25,70]
c1 = [3, 3, 3]

kalian = list(map(kali, a1[0:2], b1[0:2]))

print(kalian)

triplet = lambda x, y ,z : x * y* z 

hasil30 = list(map(triplet, a1, b1, c1))

print(hasil30)

print("="*50)

# FILTER FUNCTION

a2 = [1,2,3,4,5,6,7,8,9,10]

hasil4 = list(filter(lambda x: x%2 == 0, a2))

print(hasil4)

print("="*50)

# REDUCE FUNCTION

from functools import reduce

print("ini nih")

f = [1,2,3,4,5,6,7,8,9,10]

hasil5 = reduce(lambda a, b: a + b, f)

print(hasil5)

print("="*50)

# Latihan 

z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# hasil4 = list(filter(lambda x: x%2 == 0, a2))

# pangkat3 = lambda x: x**3

hasilpangkat3 = list(map(lambda x: x**3, z))

print(hasilpangkat3)

hasilatihan = list(filter(lambda x: x >= 1 and x <= 200,filter(lambda x: x%2 == 0, map(lambda x: x**3, z))))

print(hasilatihan)




