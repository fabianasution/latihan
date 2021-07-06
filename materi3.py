# hari = ["senin", "selasa", "rabu" , "kamis",  "jumat", "sabtu", "minggu" ]

# counter = 0 

# for i in hari:
#     print (i)
    
     
    

# print ("=" *50)

# while counter <7  :

#     print (hari[counter])
#     counter += 1

# a = 2 
# b = 2
# print(hari.index("sabtu"))

# print(hari [a + b])

hari1 = ["senin", "selasa", "rabu" , "kamis",  "jumat", "sabtu", "minggu" ]

hari1.append("sunday") # Hari di tambahkan di paling terakhir

print(hari1)

hari1.insert(4, "Thursday")

print(hari1)

hari1[1] = "tuesday"

print(hari1)

hari1.remove("senin")

print(hari1)

# hari1.pop(0)
# print(hari1)



harienglish = list()

harienglish.append(hari1[1])
harienglish.append(hari1[4])
harienglish.append(hari1[0])

harienglish.append(hari1) 

# ['kamis', 'sabtu', 'rabu', ['rabu', 'kamis', 'Thursday', 'jumat', 'sabtu', 'minggu', 'sunday']] = harienglish

print(harienglish)

print(harienglish[3][0])

harienglish.pop(3)
print(harienglish)

angka = [ 8, 9, 70, 89, 90, 86, 67, 123, 5]

angkaterbesar = max(angka)
angkasum = sum(angka)
angkalowest = min(angka)
urutangka = angka.sort()
urutkebalik = angka.sort(reverse=True)


print(angkaterbesar)

# tupple 

listtup = 1, 2, 4, 6, 8, 9, 5, 765

print(type(listtup))

setdata = {}
print(type(setdata))
#set
setdata1 = set()
print(type(setdata1))

setdat = []
print(type(setdat))

#Dictionary 

nilai = {
    "fabian" : 85, 
    "budi"   : 70,
    "rastra" : 90,
}

print(nilai["budi"])
print(type(nilai))

nilai.keys() #seluruh keys dictionary 
nilai.values()  #seluruh value 
nilai.items() #seluruh gabungan 
nilai.pop("budi") #hapus data 


nilai["hutagalung"] = 90 # create or update data 

print(nilai.items())

# Function 



# def rumus1(contoh):
#     if contoh%2 == 0:
#         print("genap")

#     else:
#         print("ganjil")

# rumus1(2)

# return function
def rumus1(contoh):
    if contoh%2 == 0:
        return "genap" 

    else:
        return "ganjil" 

print(rumus1(2))

input = "budi septian"

input1 = input.split(" ")

print(input1)