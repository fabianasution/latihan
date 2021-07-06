input1 = input("masukan kata yang diinginkan: ")
input2 = input1.replace(" ","")
import re


def rumus(nilai):
    
    counter = len(nilai)

    return(counter)

counter2 = rumus(input2)

try:
    def triangle(inputdalem):
      
        if counter2 == 1:
            counter1 = 1
        elif counter2 == 3:
            counter1 = 2

        elif counter2 == 6:
            counter1 = 3

        elif counter2 == 10:
            counter1 = 4

        elif counter2 == 15:
            counter1 = 5

        elif counter2 == 21:
            counter1 = 6

        elif counter2 == 28:
            counter1 = 7

        elif counter2 == 36:
            counter1 = 8

        elif counter2 == 45:
            counter1 = 9
        
        elif counter2 == 55:
            counter1 = 10

        else:
            print("Mohon maaf, Jumlah karakter tidak memenuhi syarat membentuk pola")

        hasil = ""

        k = 0
        for a in range(0,(counter1 +1)):
            for b in range(0, a):
                hasil = print(inputdalem[k], end=" ")
                k= k+1
            print ()

        k=0
        for i in range((counter1 +1),1,-1):
            for j in range(1,i):
                hasil = print(inputdalem[k],end=" ")
                k = k+1
            print()

        

            


    triangle(input2)

except:

        print()








