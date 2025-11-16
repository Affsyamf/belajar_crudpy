from . import Database
from . Util import random_string
import time
from . import Database


def update(no_tugas,pk,date_at,judul,deskripsi,assign):
    data = Database.TEMPLATE.copy()
    
    data["pk"] = pk
    data["date_at"] = date_at   
    data["judul"] = judul 
    data["deskripsi"] = deskripsi 
    data["assign"] = assign
    
    data_str = f'{data["pk"]}, {data["date_at"]}, {data["judul"]}, {data["deskripsi"]}, {data["assign"]}\n'

    panjang_data = len(data_str)
    
    try:
        with (open(Database.DB_NAME,'r+',encoding="utf-8")) as file:
            file.seek(panjang_data*(no_tugas-1))
            file.write(data_str)
    except:
        print("Eror update")
    
def create(judul, deskripsi, assign):
    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_at"] = time.strftime('%Y-%m-%d-%H-%M-%S%z',time.gmtime())   
    data["judul"] = judul 
    data["deskripsi"] = deskripsi 
    data["assign"] = assign
    
    data_str = f'{data["pk"]}, {data["date_at"]}, {data["judul"]}, {data["deskripsi"]}, {data["assign"]}\n'
    
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal Tambah Data")

def create_first():
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
    
    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_at"] = time.strftime('%Y-%m-%d-%H-%M-%S%z',time.gmtime())   
    data["judul"] = judul 
    data["deskripsi"] = deskripsi 
    data["assign"] = assign
    
    data_str = f'{data["pk"]}, {data["date_at"]}, {data["judul"]}, {data["deskripsi"]}, {data["assign"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("gagal")
        
def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_tugas = len(content)
            if "index" in kwargs:
                index_tugas = kwargs["index"]-1
                if index_tugas < 0 or index_tugas > jumlah_tugas:
                    return False
                else:
                    return content[index_tugas]
            else:
                return content
            
    except:
        print("eror membaca")
        return False
        