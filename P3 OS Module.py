print("\n<<<<<<<-----------------welcome to directory----------------->>>>>>>\n".title())
#print("\nHelp center:")
print("1 -> create director".title())
print("2 -> list directory".title())
print("3 -> show current directory".title())
print("4 -> delete folder".title())
print("5 -> create file".title())
print("6 -> delete file".title())
print("7 -. Exit\n")

while(True):
    import os


    n=int(input("\nSelect Option : "))

    if(n==1):
        newfolder = input("Enter Folder Name : ").strip().lower()
        makedir = os.mkdir(newfolder)
        print("\nFolder Created Successfully...")
        print("\n*****************************************************************************")

    elif(n==2):
        print("\n---------------------List Of Directory---------------------")
        print(*os.listdir(), sep = '\n')
        print("\n*****************************************************************************")
    elif(n==3):
        currentdir = os.getcwd()
        print("\nCurrent Directory -> ",currentdir)
        print("\n*****************************************************************************")

    elif(n==4):
        deletefolder = input("Enter Folder Name Delete : ").strip().lower()
        removefolder = os.rmdir(deletefolder)
        print(f"\n< '{deletefolder}' folder is Deleted Succeddfully >")
        print("\n*****************************************************************************")

    elif(n==5):
        name = input("Enter Name Of File With Extension, e.g(.txt,.py,.html, etc) : ")
        file = open(f"{name}","w")
        content = input("enter content here : ".title())
        cont = file.write(content)
        print(f"\n< File {name} Created Successfully >")
        print("\n*****************************************************************************")
        file.close()

    elif(n==6):
        deletefile = input("\nEnter file name you want to delete : ".title()).strip().lower()
        removefile = os.remove(deletefile)
        print(f"\n< '{deletefile}' file is Deleted Succeddfully >")
        print("\n*****************************************************************************")

    elif(n==7):
        ext=input("\nare you sure, you want to exit? (Y/N): ".title())
        if(ext.lower()=="y"):
            print("\n<<<<<<<-----------------Thank you----------------->>>>>>>")
            break
        elif(ext.lower()=="n"):
            continue
        else:
            print("Something Went Wrong... \nPlease Try Again.")
           

    































        
        
        
        
