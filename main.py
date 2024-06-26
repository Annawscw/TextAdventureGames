#functions

def Scene2():
    print ("As you go deeper into the forest you trip on something quite bulky.")
    print ("You check what it is you tripped on.")
    print ("It seems to be a chest!")
    print ("Would you like to open the chest?")
    choice = input("> ")
    if choice == "no":
         print("You walk away")
    elif choice == "Yes":
         print("The chest contains a sword and gold.")

def Scene3():
    print("Would you like to take the gold and the sword?")
    choice = input("> ")
    if choice == "yes":
        print ("You take the gold and sword and walk further into the forest.")
    elif choice == "no":
        print("You walk further into the forest")

def Scene4():
    print ("As you walk further into the forest and come across two paths, one going to the left and one going to the right.")
    print("Which way would you like to go?")
    choice = input("> ")
    if choice == "right":
        print("You wander deeper into the forest")
    elif choice == "left":
        print("")
       
    


    

    




#main code
Scene2()
Scene3()
Scene4()
