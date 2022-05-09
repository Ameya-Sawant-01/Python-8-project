class user():
    count=0
    def __init__(s, name, gender, salary, adhar):
        s.name = name
        s.gender = gender
        s.salary = salary
        s.adhar = adhar
        user.count+=1
        
    def  showdetails(s):     
        print("Name : ",s.name)
        print("Gender : ",s.gender)
        print("Salary : ",s.salary)
        print("Adhar No: ",s.adhar  )
        print(f"Account No : {s.adhar*2-199}\n")

class bank(user):

    def __init__(s,name,gender,salary,adhar):
        super().__init__(name,gender,salary,adhar)
        s.__balance = 0
      
            
    def  deposite(s,amount):
        s.__balance+=amount
        print(f"\n{amount} deposited in your account \nCurrent Account Balance : Rs ",s.__balance)
        print("\n---------------------------------------------------------------------------")

    def withdraw(s,amount):
        if(amount>s.__balance):
            print("\nInsufficient Balance \nAvailable Balance : ",s.__balance)
        elif (amount>=100)and (amount<=s.__balance) and (amount%100==0):
            s.__balance=s.__balance-amount
            print(f"\n{amount} rs is Withdrawed from Your Account \nCurrent Account Balance : ")
            print("\n---------------------------------------------------------------------------")
        elif amount<100 or (amount%100!=0):
            print(f"\nPlease Enter Amount Multiple of 100")
            
    def viewbalance(s):
        #print(s.showdetails())
        print("\nAccount Balance : \n",s.__balance)
        print("\n---------------------------------------------------------------------------")
        

    def transfer(s, amount, user):
        if(amount>s.__balance):
            print("Insufficient balance\nPlease Try Again")
            print("\n---------------------------------------------------------------------------")
        elif (amount>=100 and amount<=s.__balance):
            s.__balance = s.__balance-amount
            print(f"\n{amount} Transfered to {user}")
            print("\nAccount Balance:",s.__balance)
            print("\n---------------------------------------------------------------------------")
        elif amount<100:
            print("You can't transfer less then 100 Rs\nCurrent Account Balance : ",s.__balance)
            print("\n---------------------------------------------------------------------------")

        
name = input("Enter name : ")
gender = input("Enter gender : ")
salary = int(input("Enter salary : "))
adhar = int(input("Enter Adhar no. : "))


abi = bank(name,gender,salary,adhar)

print(f"\n--------------Welcome {name} In ABI Bank --------------\n")
s = input("\nShow Personal Details (Y/N) : ")
if s.lower()=='y':
    print(abi.showdetails())
    print(f"Hey {name}, Welcome!!! \nNice To Meet You Here...")
else :
    print(f"Hey {name}, Welcome!!! \nNice To Meet You Here...")

print("\n")
print("Select 1 for DEPOSIT")
print("Select 2 for WITHDRAW")
print("Select 3 for TRANSFER")
print("Select 4 for VIEW BALANCE")
print("Select 5 for EXIT\n")



while(True):
    move = input("\nEnter your choice  : ")
    if move.lower()=="1":
        amount = int(input("Enter Amount : "))
        abi.deposite(amount)
        
    elif move.lower()=="2":
        amount = int(input("Enter Amount : "))
        abi.withdraw(amount)
        
    elif move.lower()=="3":
        amount = int(input("Enter Amount : "))
        user = input("Enter Name : ")
        abi.transfer(amount,user)
        
    elif move.lower()=="4":
        abi.viewbalance()
        
    elif move.lower()=="5":
        ex = input("Are You Want To EXIT (Y/N) : ")
        if ex.lower()== "y" :
            print("Thank You For Visiting")
            break
        else:
            continue
    else :
        print("Someting Went Wrong \nPlease Try Again\n ")
        
    



    
