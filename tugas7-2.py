# nomer 2 

operator = "+-*/"

def kalkulator(i1, i2, i3):
    try:
        if (any((c in operator) for c in i3)):
            if i3 == "*":
                hasil = i1 * i2
                return (f"\nhasil perkalian dari {i1} dan {i2} adalah {hasil}\n")
            
            elif i3 == "+":
                hasil = i1 + i2
                return (f"\nhasil penjumlahan dari {i1} dan {i2} adalah {hasil}\n")

            elif i3 == "-":
                hasil = i1 - i2
                return (f"\nhasil pengurangan dari {i1} dan {i2} adalah {hasil}\n")

            elif i3 == "/":
                hasil = i1 / i2
                return (f"\nhasil pembagian dari {i1} dan {i2} adalah {hasil}\n")

        else:
            return("\noperator yang anda masukan tidak sesuai\n")
    except:
        return("\nInput yang anda masukan salah\n")


try:
    input1 = int(input("masukan angka pertama:"))
    input2 = int(input("masukan angka pertama:"))
    input3 = input("masukan operator yang anda inginkan (+-*/) :")

    print(kalkulator(input1, input2, input3))

except:
    print("\nInput angka yang anda masukan salah\n")     


