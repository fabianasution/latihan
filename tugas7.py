import sys
# Nomer 1

kata = input("Masukan kalimat yang ingin anda decode/encode (bila kode morse dipisahkan dengan | : ")

kata = kata.lower()

char = "abcdefghijklmnopqrstuvwxyz"
morse = "._"


def split(word):
    return [char for char in word]

database = {
    "a" : ". _",
    "b" : "_ . . .",
    "c" : ". .  .",
    "d" : "_ . .",
    "e" : ".",
    "f" : ". _ .",
    "g" : "_ _ .",
    "h" : ". . . .",
    "i" : ". .",
    "j" : "_ . _ .",
    "k" : "_ . _",
    "l" : "___",
    "m" : "_ _",
    "n" : "_ .",
    "o" : ".  .",
    "p" : ". . . . .",
    "q" : ". . _ .",
    "r" : ".  . .",
    "s" : ". . .",
    "t" : "_",
    "u" : ". . _",
    "v" : ". . . _",
    "w" : ". _ _",
    "x" : ". _ . .",
    "y" : ". .  . .",
    "z" : ". . .  .", 
    " " : " "
}


def morsedecode (inputkata):
    
    value1 = list(database.values())
    key1 = list(database.keys())

    if (any((c in char) for c in inputkata)) and (any((c in morse) for c in inputkata)):
        print("\nInput yang anda masukan salah hanya bisa kata tau morse tidak bisa di gabung\n")
        sys.exit()

    elif (any((c in char) for c in inputkata)) and (any((c in morse) for c in inputkata) == False):
        pisah = split(inputkata)
        jumlahkat = len(pisah)

        print("Hasil decode/encode dari kalimat yang anda masukan adalah:\n")
        
        for i in range (0 , jumlahkat):
            print(database[pisah[i]], end="|")
        print()

    elif (any((c in morse) for c in inputkata)):

        inputkata1 = inputkata.split("|")

        jumlahkat = len(inputkata1)

        print("\nHasil decode/encode dari kalimat yang anda masukan adalah:")


        for i in range (0 , jumlahkat):
            kata1 = value1.index(inputkata1[i])

            print(key1[kata1], end="")
        print()

    else:
        print("\ninput yang ada angka, hanya bisa memasukan kode morse atau kalimat\n")


try:
    morsedecode(kata)

except:
    print("Input yang anda masukan bukan kode morse")



