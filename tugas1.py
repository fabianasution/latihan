## Number 1 

jumlahkaki = 32
jumlahbinatang = 13
jumlahkakiayam = 2
jumlahkakikam = 4

ayam =int( (jumlahkaki - ( jumlahbinatang * jumlahkakikam ))/ (-jumlahkakiayam) )
kambing = int (jumlahbinatang - ayam)

print(f"Adam memiliki ayam {ayam} ekor dan kambing {kambing} ekor")

print("\n" * 1)

## Number 2 

dulu = 19 
ibu = ((dulu / 7)+ (1/2)) / (3/28)
anak = 1/4 * ibu - 1/2


ibumelahirkan = int(ibu - anak)

print(f"Umur ibu sat melahirkan anak adalah {ibumelahirkan} " )

print("\n" * 1)

## Number 3

ayahbudi = 50
duluayahbudi = 42
ayahdulu = (duluayahbudi/7) * 6 
ayah = int(ayahdulu + 4)
budi = int(ayahbudi - ayah)

print(f"Usia ayah saat ini adalah {ayah} tahun, dan usia budi saat ini adalah {budi} tahun")

print("\n" * 1)

#number 4 

kalimat = str(input("masukan kalimat anda: "))
karakter = str(input("karakter pilihan anda: "))


string = "Python Is awesome, isn't it?"
substring = "i"

count = int(kalimat.count(karakter))
count1 = int(kalimat.count(karakter.upper()))


print("Jumlah karakter:", karakter, " \ndidalam kalimat:", kalimat, "\nadalah:", count+count1)

print("\n" * 1)

#number 5

inputkalimat = str(input("masukan kalimat anda: "))
inputvokal = str(input("karakter pilihan anda: "))


step1 = inputkalimat.replace("a", inputvokal)
step2 = step1.replace("A", inputvokal)
step3 = step2.replace("i", inputvokal)
step4 = step3.replace("I", inputvokal)
step5 = step4.replace("u", inputvokal)
step6 = step5.replace("U", inputvokal)
step7 = step6.replace("e", inputvokal)
step8 = step7.replace("E", inputvokal)
step9 = step8.replace("o", inputvokal)
step10 = step9.replace("O", inputvokal)

print("output :", step10)

print("\n" * 1)

#Number 6 

A = int(input("masukan kecepatan mobil A: "))
B = int(input("masukan kecepatan mobil B: "))
jarak = 120
waktu = 60 

print("Jarak antara kedua mobil tersebut adalah", jarak, "KM")
print("Kecepeatan mobil A adalah", A, "KM/jam")
print("Kecepeatan mobil A adalah", B, "KM/jam")

hasil = jarak - A - B

kalian = 1.0

while hasil > 0 :
    kalian = kalian + 0.1
    a = A * kalian
    b = B * kalian
   

    hasil = jarak - a - b
    


totalwaktu = waktu * kalian
TW = totalwaktu // 60
TM = totalwaktu % 60 
totaljam = int(TW)
totalminute = int(TM)
print("total waktu yang di temput adalah", totaljam, "jam", totalminute, "menit") 




