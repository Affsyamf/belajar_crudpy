from . import Operasi
from . import read_console

def create_console():
    print("\n\n"+"="*100)
    print("Tambah Task : \n")
    judul = input("Judul : ")
    deskripsi = input("Deskripsi : ")
    
    while(True):
        assign = input("Diberikan ke : ")
        if not assign.isalpha():
            print("Assign harus huruf")
            continue
        else:
            print("Ok", assign)   
            break     
        
    Operasi.create(judul, deskripsi, assign)
    print(f"\nData Baru masuk")
    read_console()