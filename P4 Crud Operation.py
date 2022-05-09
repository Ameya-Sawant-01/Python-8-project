

def createfile(ids,name,age,place,salary):
    
    
    file=open("login.txt","w")
    data=[]
    record=[ids,name,age,place,salary]
    data.append(record)
    

    for i,n,a,p,s in data:
        file.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^5}\n")
        
    file.close()
     

def addr():
    
    ids = input("Enter Id: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    place = input("Enter Place: ")
    salary = input("Enter Salary: ")
    file=open("login.txt","a")
    d=ids,name,age,place,salary
    file.write(f"{d[0]:^3} {d[1]:^8} {d[2]:^3} {d[3]:^10} {d[4]:^5}\n")
    file.close()
    print("Data Added Successfully...!!!")


def ShowRec():
    
    file = open("login.txt","r")
    record = file.readlines()
    file.close()
    for d in record:
        print(d)


def updaterec(*args): 

    ShowRec()
    b = createfile(ids,name,age,place,salary)
    print(b)
   
    

def dele(ids):
    f = open("login.txt","r")
    record = f.readlines()
    f.close()

    newdata=[]

    for d in record:
        x = d.strip().split()
        newdata.append(x)

    ids = int(ids)

    ids = newdata[ids-1][0]
    name = newdata[ids-1][1]
    age = newdata[ids-1][2]
    place = newdata[ids-1][3]
    salary = newdata[ids-1][4]

    newdata.pop(ids-1)

    f = open("login.txt","w")

    for i,n,a,p,s in newdata:
        f.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^5}\n")
    f.close()

    
    
##    id=int(input("Enter Id : "))
##    file=open("login.txt","r")
##    l=file.readlines()
##    
##    file=open("login.txt","w")
##    for i in l:
##        for i,n,a,p,s in l:
##            file.write(f"{i:^3} {n:^8} {a:^3} {p:^10} {s:^5}\n")
##            l.pop(id-1)
##            print("Deleted Successfully...")   
##    file.close()



while(True):
    print("Select 1 - Create Record")
    print("Select 2 - Show Record")
    print("Select 3 - Update Record")
    print("Select 4 - Delete Record")
    print("Select 5 - Add Record")
        

    operation=int(input("Proceed: "))
    print()

    if(operation==1):
        ids = input("Enter Id: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        place = input("Enter Place: ")
        salary = input("Enter Salary: ")
        
        createfile(ids,name,age,place,salary)
        print("\nData Inserted Successfully!!!")
        print("-----------------------------------------------------------")
        ShowRec()
        print("-----------------------------------------------------------")


    elif(operation==2):
        print("\nYour Current Data")
        print("-----------------------------------------------------------")
        ShowRec()
        print("-----------------------------------------------------------")
      


    elif(operation==3):
        ShowRec()
        ids = input("Enter Id: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        place = input("Enter Place: ")
        salary = input("Enter Salary: ")
        
        updaterec(ids,name,age,place,salary)
        print("Data Updated Successfully!!!")
        print("-----------------------------------------------------------")
        ShowRec()
        print("-----------------------------------------------------------")
        

    elif(operation==4):
        ShowRec()
        dele(ids)
        

    elif(operation==5):
        ShowRec()
        addr()















