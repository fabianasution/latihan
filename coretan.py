# import re 
# import sys
# from typing import Dict

# # input1 = "fabian nasution!"

# # cek1 = any(char.isdigit() for char in input1)
# # print(cek1)

# # def hasNumbers(inputString):
# #    return any(char.isdigit() for char in inputString)

# # namacek = hasNumbers(input1)

# # print(namacek)

# # if namacek == True:
# #     print("nama jagan menggunakan nomer atau spesial character")

# # testinput = input("pilih (y/x): ")
# # testinput1 = testinput.lower()

# # def main():

# #     print("budi doremi")

# # if testinput1 == "y" :
# #         main()

# # else:
# #     sys.exit()

# abjad = set("ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyz")
# kapital = set("ABCDEFGHIJKLMNOPRSTUVWXYZ")
# hurufkecil = set("abcdefghijklmnoprstuvwxyz")
# angka = set("1234567890")
# spesial = set("&^%$#!@")



# # def password(inputuserid):
# #     global spesial
# #     cekuser = inputuserid.isalnum()


# #     if (any((c in kapital) for c in inputuserid)) and (any((c in spesial) for c in inputuserid)) and (any((c in hurufkecil) for c in inputuserid)) and (any((c in angka) for c in inputuserid)) and len(inputuserid) >= 8 :
# #         return('\nformat benar\n')

# #     return "Password tidak sesuai format"



# # print("Ketentuan membuat pasword\n1. Terdapat huruf kapital dan kecil\n2. Terdapat spesial karakter dan angka\n3. Minimal 8 karakter")

# # inputpass = input("Masukan password yang anda inginkan sesuai ketentuan: ")

# # print(password(inputpass))


# # Nama : .... (Hanya Alfabet dan Spasi)
# # Gender : ... (Hanya bisa Female atau Male .... Pria - wanita)
# # Usia : ... (Harus Integer, Minimal 17 tahun, maksimal 80 tahun)
# # Pekerjaan : .... (Hanya alfabet dan spasi)
# # Hobi : .... (hanya alfabet dan isi lebih dari satu)
# # Alamat : 
# #     Nama Kota : (hanya alfabet dan spasi)
# #     RT : (Numerik Integer)
# #     RW : (Numerik Integer)
# #     Zip COde : (Numerik Integer dan 5 karakter)
# #     Geo : 
# #         Lat : .... Numerik - Float/Integer
# #         Longitude : .... Numerik - Float/Integer
# # No HP : ... Harus Integer, Jumlah karakter 11 - 13

# # Simpan Data (Y/N) :

# # Y : Data tersimpan
# # N : data tidak tersimpan 
# # userbaru = "fabian"

# userbaru = str()

# userbaru1 = input("nama: ")


# userbaru = userbaru1

# datauser = {userbaru : { 
#             "password" : "password1",
#             "nama" : "nama1", 
#             "gender" : "gender1",
#             "usia" : "usia1",
#             "pekerjaan" : "pekerjaan1",
#             "hobi" : "hobi1",
#             "alamat" : { 
#                 "nama kota" : "namakota1",
#                 "rt" : "rt1",
#                 "rw" : "rw1",
#                 "kodepos" : "kodepos1",
#                 "geo" : {
#                     "lat" : "lat1",
#                     "long" : "long1",}
#             },
#             "hp" : "hp1"

# }}

# userbaru = userbaru1

# print("\n")

# print(datauser)
# print("\n")
# datausertest = dict()

# print(datausertest)

# print("\n")

# datausertest.update(datauser)

# print("\n")
# print(datausertest)

# user = userbaru

# print("\n")
# print(datausertest[user]["alamat"]["geo"]["lat"])

# print("\n")

# datauserbaru = {"budi" : { 
#             "password" : "password2",
#             "nama" : "nama2", 
#             "gender" : "gender2",
#             "usia" : "usia2",
#             "pekerjaan" : "pekerjaan2",
#             "hobi" : "hobi2",
#             "alamat" : { 
#                 "nama kota" : "namakota2",
#                 "rt" : "rt2",
#                 "rw" : "rw2",
#                 "kodepos" : "kodepos2",
#                 "geo" : {
#                     "lat" : "lat2",
#                     "long" : "long2",}
#             },
#             "hp" : "hp2"

# }}

# datausertest.update(datauserbaru)

# print("\n")
# print(datausertest)


# print("\n")
# print(datausertest["budi"]["alamat"]["geo"]["lat"])






# # posisi = datausertest.index("fabian")

# # print(posisi)


# def main():

#     test = input("nomor:")
#     def budi():
#         print("main")

#     if test == "1":
#         budi()

#     else:
#         print("wow")


# main()




# stokbarang = {"royco" : 20 

# }

# inputbrang = input("\nNama barang yang mau di hapus: ")
# inputbrang = inputbrang.lower()


# try:
#     if (any((c in inputbrang) for c in stokbarang)):
        
#         updatebaranggak = input("Apakah anda ingin menghapus barang (Y/N):")
#         updatebaranggak = updatebaranggak.lower()

#         if updatebaranggak == "y":
#             stokbarang.pop(inputbrang)
        
#         elif updatebaranggak == "n":
#             print("Tidak jadi melakukan update")

#         else:
#             print("Anda salah melakukan input")

#     else:
#         print("Barang tidak ada di database")

        


#     for key, value in stokbarang.items():
#         print(key, ' : ', value)

# except:
#     print("format barang salah")

# for i in range (0, 5):
#     for x in range (5, i, -1):
#          print(x, end=" ")

#     print()

# u = 0
# for i in range (9, 5,-1):
#     u = u + 1
#     print(" " * (i - 3), "*" * u, " " * (i - 3))

# u = 5
# for i in range (3, 7):
#     u = u - 1
#     print(" " * (i), "*" * u, " " * (i))

kata = ["budi" , "fabian"]
kata1 = "fabian"

# print(f"{kata}{kata1}")


kata[0]= "wow"

print(kata)

# nilai["login"].update({"password" : "secret"})

database = {
            "senin" : 1,
            "selasa" : 2,
            "rabu" : 3,
            "kamis" : 4,
            "jumat" : 5,
            "sabtu" : 6,
            "minggu" : 7
        }


database.update({"wow" : 8})

print(database)






    