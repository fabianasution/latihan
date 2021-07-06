

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

   

