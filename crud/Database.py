from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk": "xxxxxx",
    "date_at": "yyyy-mm-dd",
    "judul":"",
    "deskripsi":"",
    "assign":""
}


def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database aman")
    except:
        print("Database error") 
        Operasi.create_first()
        
            
            