import os 

if __name__ == "__main__":
    sistem_operasi = os.name
    
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
        
        user_option = input("Masukan pilihan 1-5 : ")
        print("\n====================================")
        
        match user_option:
            case "1": print("Read Data")
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")

        print("\n====================================")
        
        lanjut = input("Lanjut ? y/n : ")
        if lanjut == "n" or lanjut == "N":
            break
        
    print("Selesai")