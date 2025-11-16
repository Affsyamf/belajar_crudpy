from . import Operasi
from . import read_console

def update_console():
    read_console()
    while(True):
        print("Pilih no tugas yang akan diedit : ")
        no_tugas = int(input("Masukan No Tugas : "))
        data_tugas = Operasi.read(index=no_tugas)

        if data_tugas:
            break
        else:
            print("Nomor tidak valid")
    
    data_break = data_tugas.split(',')
    pk = data_break[0]
    date_at = data_break[1]
    judul = data_break[2]
    deskripsi = data_break[3]
    assign = data_break[4]
    
    while(True):
        # data yang ingin diubah
        print("\n"+"="*100)
        print("Pilih no yang akan diubah : ")
        print(f"1. Judul {judul:.30}")
        print(f"2. Deskripsi {deskripsi:.40}")
        print(f"3. Diberikan Ke -  {assign:.15}")
    
        # user pilih mode untuk update
        user_option = input("Pilih data : ")
        
        match user_option:
            case "1": judul = input("Judul : ")
            case "2": deskripsi = input("Deskripsi : ")
            case "3":
                while(True):
                    assign = input("Diberikan ke : ")
                    if not assign.isalpha():
                        print("Assign harus huruf")
                        continue
                    else:
                        print("Ok", assign)   
                        break    
            case _: print("Index tidak cocok")
            
        print("Data Baru anda : ")
        print(f"1. Judul {judul:.30}")
        print(f"2. Deskripsi {deskripsi:.40}")
        print(f"3. Diberikan Ke -  {assign:.15}")
            
        lanjut = input("Selesai Update (y/n): ")
        if lanjut == "y" or lanjut == "Y":
            break
    
    Operasi.update(no_tugas,pk,date_at,judul,deskripsi,assign)
    