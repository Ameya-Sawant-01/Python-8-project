def read(r):
    file=open(r,"r")
    cont=file.read()
    file.close()
    print(cont)
    
def write(w,insert):
    file=open(w,"w")  
    file.write(insert)
    file.close

def append(a,insert):
    file=open(a,"a")
    file.write(insert)
    file.close()



while True:
    
    print("Select 1 to Read  File")
    print("Select 2 to Write File")
    print("Select 3 to Create New file")
    print("Select 4 to EXIT\n")

    choice=input("Enter your choice : ").strip()
    print()

    if choice=='1':
        r=input("Enter file name with extension : ").strip()
        print("Happy Reading...")
        read(r)
        print("\n_________________________________________________________\n")
        
        
    elif choice=='2':
        w=input("Enter Existing File Name With Extension : ").strip()
        print(f"Opened {w} File\n")
        insert=input("Write Your Content : ")
        write(w,insert)
        print(f"Content {w} has been Saved Successfully\n")   
        print("\n_________________________________________________________\n")


    elif choice=='3':
        a=input("Enter New File Name with Extension : ").strip()
        print(f"New File {a} has been Created Successfully\n")
        insert=input("Write Your Content : ")
        append(a,insert)
        print(f"Content {a} has been Saved Successfully\n")
        print("\n_________________________________________________________\n")

    elif choice=='4':
        ex = input("Do you really want to exit (Y/N) : ")
        if ex.lower()== "y":
            print("-----------------------------Thank You-----------------------------")
            break
        else:
            print("\n_________________________________________________________\n")
            continue
        
        
    else:
        print("Sorry...! \nSomething Went Wrong \nPease Enter Correct Choice.\n")

    
    
