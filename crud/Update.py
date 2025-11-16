from . import Operasi
from . import read_console

def update_console():
    read_console()
    no_tugas = int(input("Masukan No Tugas : "))
    data_tugas = Operasi.read(index=no_tugas)
    print(data_tugas)
    
    
    
    