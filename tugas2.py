#Nomer 1
try:
    Jumlahhari = int(input("Masukan Jumlah Hari yang anda mau: "))

    while Jumlahhari > 4000:
        print("Jumlah Hari diatas batas maksimal")
        Jumlahhari = int(input("Masukan Jumlah Hari yang anda mau: "))
        
    while Jumlahhari < 0:
        print("Jumlah Hari dibawah batas minimum")
        Jumlahhari = int(input("Masukan Jumlah Hari yang anda mau: "))

    tahun = Jumlahhari // 365

    sisatahun = Jumlahhari %365
    
    bulan = sisatahun // 30

    hari = sisatahun % 30 
    
    print(f"Hasil dari jumlah hari yang anda masukan adalah {tahun} Tahun {bulan} Bulan {hari} hari")

except :
     print("Jumlah hari yang ada masukan salah ")

print("\n" * 1)



#Nomer 2

try :
    beratbadan = int(input("Masukan berat badan anda (KG): "))
    tinggibadan = int(input("Masukan tinggi badan anda (CM): "))

    if beratbadan < 0 or tinggibadan < 0 :
        print("berat badan atau tinggi badan tidak bisa negatif")
        exit()

    elif beratbadan > 250 or tinggibadan >300 : 
        print("Batas maksimal berat : 250 KG dan Batas maksimal tinggi : 300 CM")
        exit()

    tinggibadan = tinggibadan / 100
    

    bmi = beratbadan / (tinggibadan ** 2)

    

    bmi = round(bmi,2)


    if bmi < 18.5 :
        print(f"Tinggi badan anda adalah {tinggibadan} M, dan berat badan anda adalah {beratbadan} KG. \nBMI anda adalah {bmi} \nMaka berat badan anda dibawah ideal")

    elif bmi >= 18.5 and bmi <= 24.9 :
        print(f"Tinggi badan anda adalah {tinggibadan} M, dan berat badan anda adalah {beratbadan} KG. \nBMI anda adalah {bmi} \nMaka berat badan anda ideal")

    elif bmi >= 25.0 and bmi <= 29.9 :
        print(f"Tinggi badan anda adalah {tinggibadan} M, dan berat badan anda adalah {beratbadan} KG. \nBMI anda adalah {bmi} \nMaka berat badan anda diatas ideal")

    elif bmi >= 30.0 and bmi <= 39.9 :
        print(f"Tinggi badan anda adalah {tinggibadan} M, dan berat badan anda adalah {beratbadan} KG. \nBMI anda adalah {bmi} \nMaka berat badan anda sangat diatas ideal")

    elif bmi >= 40.0 :
        print(f"Tinggi badan anda adalah {tinggibadan} M, dan berat badan anda adalah {beratbadan} KG. \nBMI anda adalah {bmi} \nMaka berat badan anda tergolong obesitas")

except :
    print("Angka yang ada masukan salah ")

print("\n" * 1)

#Nomer 3 

try:
    nilai = float(input("Masukan nilai anda (apabila niali ada koma menggunakan titik): "))

    if nilai > 100 :
        print("Nilai Maksimum adalah 100, nilai diatas batas maksimal")

    elif nilai >= 90 :
        print(f"Nilai anda adalah {nilai}, maka mendapatkan grade A")

    elif nilai >= 85:
        print(f"Nilai anda adalah {nilai}, maka mendapatkan grade A-")

    elif nilai >= 80:
        print(f"Nilai anda adalah {nilai}, maka mendapatkan grade B")

    elif nilai >= 75:
        print(f"Nilai anda adalah {nilai}, maka mendapatkan grade B-")

    elif nilai >= 70:
        print(f"Nilai anda adalah {nilai}, maka mendapatkan grade C")
    
    elif nilai >= 65:
        print(f"Nilai anda adalah {nilai}, maka mendapatkan grade D")

    elif nilai >= 40 and nilai < 65 :
        print(f"Nilai anda adalah {nilai}, maka anda perlu remedial")
    
    elif nilai < 40 and nilai >= 0:
        print(f"Nilai anda adalah {nilai}, maka anda dinyatakan tidak lulus")

    elif nilai < 0  :
        print("Nilai Minimun adalah 0, tidak menerima angka negatif")

    


except:
    print("Angka yang anda masukan salah")

print("\n" * 1)




