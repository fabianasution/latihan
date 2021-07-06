try: 
    inputhari = input("Masukan Hari yang anda inginkan: ")
    angka = int(input("Masukan angka yang anda inginkan: "))
    inputhari = inputhari.lower()



    database = {
            "senin" : 1,
            "selasa" : 2,
            "rabu" : 3,
            "kamis" : 4,
            "jumat" : 5,
            "sabtu" : 6,
            "minggu" : 7
        }

    namahari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

    if inputhari not in database:
        print("Input yang anda masukan bukan hari")

    else:
        urutan = database[inputhari]
        urutanfinal = urutan + angka
        

        if urutanfinal < 0:
            urutanfinal1 = urutanfinal + 7 - 1
            harifinal = (namahari[urutanfinal1])
            print(f"\n{angka} hari dari hari {inputhari} adalah hari {harifinal}")

        elif urutanfinal > 7:
            urutanfinal1 = urutanfinal - 7 - 1
            harifinal = (namahari[urutanfinal1])
            print(f"\n{angka} hari dari hari {inputhari} adalah hari {harifinal}")

        else:
            harifinal = (namahari[urutanfinal-1])
            print(f"\n{angka} hari dari hari {inputhari} adalah hari {harifinal}")

except:


    print("Input kedua yang anda masukan harus angka")