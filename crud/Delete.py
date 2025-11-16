from . import Operasi
from . import read_console
from . import Database

def delete_console():
    read_console()
    while (True):
        no_tugas = int(input("Nomor Tugas : "))
        data_tugas = Operasi.read(index=no_tugas)
        
        if data_tugas:
            data_break = data_tugas.split(',')
            pk = data_break[0]
            date_at = data_break[1]
            judul = data_break[2]
            deskripsi = data_break[3]
            assign = data_break[4]
                    
            print("\n"+"="*100)
            print("Data yang ingin anda hapus")
            print(f"1. Judul : {judul:.40}")
            print(f"2. Deskripsi : {deskripsi:.30}")
            print(f"3. Diberikan Ke -  : {assign:20}")
            lanjut = input("Apakah anda yakin (y/n) : ")
            if lanjut.lower() == 'y':
                Operasi.delete(no_tugas)
                break
        else:
            print("Nomor tidak valid")
        
    print("Data berhasil di hapus")
        
        