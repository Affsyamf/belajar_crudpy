import os 
import crud as crud

if __name__ == "__main__":
    sistem_operasi = os.name
    
    match sistem_operasi:
        case 'posix':os.system("clear")
        case 'nt': os.system("cls")
        
    print("Selamat datang di Task Management")
    print("Database Task Management")
    print("====================================")
    
    # check database itu ada atau tidak
    crud.init_console()
    
    while(True):
        match sistem_operasi:
            case 'posix':os.system("clear")
            case 'nt': os.system("cls")
            
        print("Selamat datang di Task Management")
        print("Database Task Management")
        print("====================================")
            
        print(f"1. Read Task")
        print(f"2. Create Task")
        print(f"3. Update Task")
        print(f"4. Delete Task")
        print(f"5. Keluar")
        
        user_option = input("Masukan pilihan 1-5 : ")
       
        match user_option:
            case "1": crud.read_console()
            case "2": crud.create_console()
            case "3": crud.update_console()
            case "4": crud.delete_console()
            case "5": print("Keluar")
            
        if user_option == "5":
            break
        
        lanjut = input("Lanjut ? y/n : ")
        if lanjut.lower() == "n":
            break
        
    print("Program Selesai Terima Kasih")