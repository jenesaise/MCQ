Playing = True 

while Playing == True:
    print("Multiple Choice Questions!")
    print()

    print("Q1 = What Is The Fastest Animal On Earth?")
    print()
    print("A = Lion")
    print("B = Cheetah")
    print("C = Tiger")
    print()
    Ans = input("Enter Your Choice = ")
    while Ans != "B":
        print("Incorrect Answer.")
        Ans = input("Re-enter Your Choice = ")
    else:
        print("Correct Answer! The Fastest Animal In The World Is The Cheetah With A Speed Of 64 mph!")
        
    print()
    print("Q2 = What Is The Most Populated City On Earth?")
    print()
    print("A = Tokyo")
    print("B = Delhi")
    print("C = New York City")
    print()
    Ans = input("Enter Your Choice = ")
    while Ans != "A":
        print("Incorrect Answer.")
        Ans = input("Re-enter Your Choice = ")
    else:
        print("Correct! The Most Populated City On Earth Is Tokyo With A Population Of Approximately 37 Million People!")
        
    print()
    print("Q3 = Which Country Has The Highest Crime Rate In The World?")
    print()
    print("A = South Africa")
    print("B = Afghanistan")
    print("C = Venezuela")
    print()
    Ans = input("Enter Your Choice = ")
    while Ans != "C":
        print("Incorrect Answer!")
        Ans = input("Re-enter Your Choice = ")
    else:
        print("Correct! Venezeula Is The  Country With The Largest Crime Rate In the World With A Crime Index Of 83.76!")
        
    print()
    print("Q4 = What Is The Most Used Application In The World?")
    print()
    print("A = WhatsApp")
    print("B = Instagram")
    print("C = YouTube")
    print()
    Ans = input("Enter Your Choice = ")
    while Ans != "A":
        print("Incorrect Answer!")
        Ans = input("Re-enter Your Choice = ")
    else:
        print("Correct! WhatsApp Is The Most Used Application In The World With Approximately 2 Billion Users!")
        
    print()
    print("Q5 = What Is The Most Played Game On Earth?")
    print()
    print("A = League Of Legends")
    print("B = Minecraft")
    print("C = GTA")
    print()
    Ans = input("Enter Your Choice = ")
    while Ans != "B":
        print("Incorrect Answer!")
        Ans = input("Re-enter Your Choice = ")
    else:
        print("Correct! Minecraft Is The Most Played Game On Earth With Approximately 140 Million Monthly Actice Users!")
        
    print()
    PlayAgain = input("Would You Like To Solve The MCQ's Again? (y/n)").lower()
    if PlayAgain == "n":
        Playing = False

print("Thank You For Solving All The Questions!")
