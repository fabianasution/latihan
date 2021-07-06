
try: 
    kata = input("Masukan kata yang anda ingin kan: ")
    angkamasuk = int(input("masukan angka yang anda ingin kan: "))
    kata = kata.lower()

    inputkata = kata.split(" ")

    char = "abcdefghijklmnopqrstuvwxyz"
    char1 = "abcdefghijklmnopqrstuvwxyz "
    morse = "._"
    spasi = " "

    database = {
        "a" : 1,
        "b" : 2,
        "c" : 3,
        "d" : 4,
        "e" : 5,
        "f" : 6,
        "g" : 7,
        "h" : 8,
        "i" : 9,
        "j" : 10,
        "k" : 11,
        "l" : 12,
        "m" : 13,
        "n" : 14,
        "o" : 15,
        "p" : 16,
        "q" : 17,
        "r" : 18,
        "s" : 19,
        "t" : 20,
        "u" : 21,
        "v" : 22,
        "w" : 23,
        "x" : 24,
        "y" : 25,
        "z" : 26, 
        " " : " "
    }

    def split(word):
        return [char for char in word]

    pisah = split(char)


    for x in range (0, len(inputkata)):

        pisah2 = split(inputkata[x])

        if (any((c in  char1) for c in inputkata[x])):
            for i in range (0,len(pisah2)):
                urutan = database[pisah2[i]] + angkamasuk
                if urutan < 0:
                    urutanfinal = urutan + 26
                    print(pisah[urutanfinal-1], end="")

                elif urutan > 26:
                    urutanfinal = urutan - 26
                    print(pisah[urutanfinal-1], end="")

                else:
                    print(pisah[urutan-1], end="")


        else:
            print("\nInput pertama hanya boleh huruf")

        print(end=" ")


    print()

except:
    print("\nHanya boleh memasukan angka pada input kedua")
        

    

        
        