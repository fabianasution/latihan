import numpy as np 

angka = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

angkanumpy = np.array(angka)

def pilihan1 (angkanum):
    angkanum1 = np.array(angkanum)
    angkatranspose = np.transpose(angkanum1)
    opsi3= np.flip(angkatranspose,1)
    return(opsi3)


def pilihan2 (angkanum):
    angkanum1 = np.array(angkanum)

    opsi2 = np.flip(angkanum1,0)
    opsi22 = np.flip(opsi2,1)
    return opsi22

def pilihan3 (angkanum):
    angkanum1 = np.array(angkanum)
    angkatranspose = np.transpose(angkanum1)
    opsi3= np.flip(angkatranspose,0)
    return(opsi3)


print(f'Matrix original:\n{angkanumpy}\n')

pilihanuser = input("masukan pilihan anda (1-3):")

if pilihanuser == "1":

    print("hasil dari pilihan anda adalah:\n")

    print(pilihan1(angka))

elif pilihanuser == "2":
    print("hasil dari pilihan anda adalah:\n")
    print(pilihan2(angka))

elif pilihanuser == "3":
    print("hasil dari pilihan anda adalah:\n")
    print(pilihan3(angka))

else:
    print("pilihan anda tidak ada dalam daftar")






