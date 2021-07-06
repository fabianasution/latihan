

hasildata = []

# print(type(hasildata))

# print(hasildata)

def datadata():

    for i in range(4):

        input1 = input("Masukan Nama: ")
        input2 = input("Masukan Mata pelajaran: ")


        data = list()
    
        data.insert(0,input1)
        data.insert(1,input2)

       
        

        a = hasildata.append(data)
        

pertanyaan = input("apakah mau menambahkan data (YES/NO): ")
pertanyaan1 = pertanyaan.upper()

if pertanyaan1 == "YES":
    datadata()

    print(f"hasil dari data yang di simpan adalah {hasildata}")


else :
    print("\nTerima Kasih")






