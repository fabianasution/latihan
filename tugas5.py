import sys
inputluar = input("masukan hari untuk di translate: ")

cekinput = inputluar.isalpha()

if cekinput == False :
    print("\nhari yang anda masukan salah, hari tidak bisa sebuah angka")
    sys.exit()

def translatorhari(input1):
    try: 
    
        input2 = input1.lower()

        hari = {"senin" : "monday", 
        "selasa" : "tuesday",
        "rabu" : "wednesday",
        "kamis" : "thursday",
        "jumat" : "friday",
        "sabtu" : "saturday",
        "minggu" : "sunday"
        }

        if input2 in hari.keys():
            return(f"\nHari yang ingin anda translate adalah {input2} , bahasa inggris nya adalah {hari[input2]}")

        else: 
            indo = list(hari.keys())
            eng = list(hari.values())

            indexeng = eng.index(input2)
            indotrans = indo[indexeng]
            return(f"\nDay that you chose is {input2}, and translated to bahasa indonesia become {indotrans}")

    except:
        return("\nHari yang anda masukan tidak ditemukan, atau bukan bahasa indonesia dan bahasa inggris")

print(translatorhari(inputluar))

