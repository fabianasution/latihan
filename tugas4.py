import re 


input1 = input("masukan email anda untuk diverifikasi: ")


print(f"Alamat email anda yang akan di cek adalah {input1}\n")


def emailseluruh(inputuser):

    try: 
        # Pemisahan email untuk di verifikasi (apakah format awal benar atau tidak)

        pemisah1 = inputuser.split("@")

        namauser = pemisah1[0]


        hostingexs = pemisah1[1]

        pemisah2 = hostingexs.split(".")

        hosting = pemisah2[0]

        extensi = pemisah2[1]

        extensi2 = ""

        

        if len(pemisah2) > 2:

            extensi2 = pemisah2[2]

            
            

        def verificationemail(Input1, NamaUser, Hosting, Pemisah2,  Extensi1, Extensi2):
            import re 
            


            if NamaUser == "":
                return("Format email anda salah tidak terdapat nama user didalam nya\n")

            inital = re.search(" ", Input1)

            if inital: 
                return("Format email anda salah terdapat spasi di dalam nya\n")

            
            if len(Pemisah2) > 3:

                return("Format extensi yang anda gunakan tidak valid\n")

            userdepan = NamaUser[0].isalpha()
            userdepan1 = NamaUser[0].isnumeric()

            if userdepan == False and userdepan1 == False :
                return("Format tidak valid karena nama user name hanya dapat di awali huruf atau angka\n")

            testhosting = Hosting.isnumeric()

            if testhosting == True:
                return("Format email invalid karena hosting tidak boleh hanya berisikan nomor\n")

            extensicek1 = Extensi1.isalpha()
            extensicek2 = Extensi2.isalpha()

            
            if extensi2 == "":

                if (len(Extensi1) > 5 or extensicek1 == False) :

                    return("Format tidak valid karena extensi anda salah\n")

            else:
                if (len(Extensi1) > 5 or extensicek1 == False) or (len(Extensi2) > 5 or extensicek2 == False):

                    return("Format tidak valid karena extensi anda salah\n")



            chars = set(''')(<>,;:\/"][}{''')

            if any((c in chars) for c in Input1):
                return('Format email anda salah terdapat special character di dalam nya\n')

            if any((c in chars) for c in NamaUser):
                return('Format email anda salah terdapat special character di dalam nya\n')

                
            else: 
                return("Alamat email anda valid\n")


        hasilakhir = verificationemail(inputuser, namauser, hosting, pemisah2, extensi, extensi2)

        return hasilakhir


    except:

        return("Format dalam email anda salah karena '@' atau extensi anda tidak valid\n")



print(emailseluruh(input1))

