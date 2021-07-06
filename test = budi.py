
A = int(input("masukan kecepatan mobil A: "))
B = int(input("masukan kecepatan mobil B: "))
jarak = 120
waktu = 60 

print("Jarak antara kedua mobil tersebut adalah", jarak, "KM")
print("Kecepeatan mobil A adalah", A, "KM/jam")
print("Kecepeatan mobil A adalah", B, "KM/jam")

hasil = jarak - A - B

kalian = 1.0

if(hasil == 0):
    
    totalwaktu = waktu * kalian
    TW = totalwaktu // 60
    TM = totalwaktu % 60 
    totaljam = int(TW)
    totalminute = int(TM)
    print("total waktu yang di temput adalah", totaljam, "jam", totalminute, "menit") 



if (hasil > 0):

    kalian = 1.0
    a = A * kalian
    b = B * kalian
   

hasil = jarak - a - b


if(hasil == 0):
    
    totalwaktu = waktu * kalian
    TW = totalwaktu // 60
    TM = totalwaktu % 60 
    totaljam = int(TW)
    totalminute = int(TM)
    print("total waktu yang di temput adalah", totaljam, "jam", totalminute, "menit")   
    

hasil = jarak - a - b    

if (hasil > 0):
    kalian1 = 1.1
    a = A * kalian1
    b = B * kalian1
   

hasil = jarak - a - b


if(hasil == 0):
    
    totalwaktu = waktu * kalian1
    TW = totalwaktu // 60
    TM = totalwaktu % 60 
    totaljam = int(TW)
    totalminute = int(TM)
    print("total waktu yang di tempuh adalah", totaljam, "jam", totalminute, "menit") 
    

hasil = jarak - a - b


if (hasil > 0):

    kalian2 = 1.2
    a = A * kalian2
    b = B * kalian2
   

hasil = jarak - a - b


if(hasil == 0):
    
    totalwaktu = waktu * kalian2
    TW = totalwaktu // 60
    TM = totalwaktu % 60 
    totaljam = int(TW)
    totalminute = int(TM)
    print("total waktu yang di tempuh adalah", totaljam, "jam", totalminute, "menit")
    



        