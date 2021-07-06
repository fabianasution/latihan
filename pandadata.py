import pandas as pd

cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000], 
        'owner': ["Fabian", "Budi", "Adrian", "Rastra"]
        }

Tablebuatan = pd.DataFrame(cars, columns = ['Brand','Price', "owner"],index=['Car_1','Car_2','Car_3','Car_4'])

print (Tablebuatan)
