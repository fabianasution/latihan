kalimat = "MAKANAN"
for i in kalimat :
    print(i.lower())

kalimat1 = input("masukan kalimat: ")
ch = input("masukan vokal: ")
for karakter in kalimat1:
    if karakter in "aiueo":
        kalimat1 = kalimat1.replace(karakter, ch.lower())

    elif karakter in "AIUEO":
        kalimat1 = kalimat1.replace(karakter, ch.upper())

print (kalimat1)

print("=" *100)


x = list()
for i in range(0, 10):
    x.append(input("masukan 10 nama yang kamu mau:"))

print(x)

sentence = ['this','is','a','sentence']
sen = ' '.join(sentence)

print(sen)

nama = ["budi", "fabian", "rastra"]
umur = [17, 18 , 19]

namabaru = " ".join(nama)

print(namabaru)

# print("=" *100)
 
# nama1 = nama
# nama1.extend(umur)

# print(nama1)

print("=" *100)




print(nama)
print(umur)

print("=" *100)
nama.append(umur)

print(nama)



