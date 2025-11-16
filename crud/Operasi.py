from . import Database
from . Util import random_string
import time
from . import Database

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
        
def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("eror membaca")
        return False
        