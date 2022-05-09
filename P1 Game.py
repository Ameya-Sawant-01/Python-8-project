class Character():
    def __init__(s, name):
        s.name = name
        s.__life = 3
        s.__score = 0

    def kick(s):
        s.__score += 10

    def punch(s):
        s.__score += 5

    def stab(s):
        s.__life -= 1

    def display_score(s):
        return s.__score

    def display_life(s):
        return s.__life

    def intro(s):
        print(f"Name    : {s.name}")
        print(f"Score   : {s.__score}")
        print(f"Life    : {s.__life}")


def start_play():
    print("---------->><<< WELCOME TO MY GAME >>><<---------\n")
    n = input("Please Enter Your Character Name : ")
    char = Character(n)

    while True:
        print("\n----------<<<<>>>>> LET'S GAME BEGIN <<<<>>>>----------")

        print("\nEnter 1 for kick")
        print("Enter 2 for Punch")
        print("Enter 3 for Stab")
        print("Enter 4 to Display Life & Score")
        print("Enter 5 for Exit")

        sel = int(input("Enter Your Choice : "))
 
        if sel == 1:
            char.kick()

        elif sel == 2:
            char.punch()

        elif sel == 3:
            stabval = char.display_life()
            char.stab()

            if stabval>1:
                continue
            else:
                print("Game Over")
                print("Score is  : ",char.display_score(),"\n")
                start_play()
                break

        elif sel == 4:
            print("\n")
            char.intro()

        elif sel == 5:
            ex = input("Are You Sure (Y/N) -->>>")
            ex = ex.lower()

            if ex == "n":
                continue
            elif ex == "y":
                break
            else:
                print("Invalid Input")
                continue


start_play()

                






















        
              
