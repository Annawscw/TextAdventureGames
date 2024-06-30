#___________________________________________
#functions

<<<<<<< Updated upstream


#main code
#functions

def intro():

# Ask the user their name 
        name=input("What's your name?")
# Greet the user and introduce the quiz
        print("Welcome to the Forest World!",name)

        answer=input("We have a thousand backgrounds for you.just give a number that you thinking now.the number must bigger than 0,less than 1000.")

            
        while True:
                try:

                    answer=input("We have a thousand backgrounds for you.just give a number that you thinking now.")
                    answer=int(answer) 
                    
                    if answer<1000 and answer >0:
                        break
                
                    if answer>1000 and answer<1:
                        print("The number should bigger than 0,smaller than 1000")  
                except:
                    
                    print("That's not a number")


        #give the background

        print("You are a very famous researcher of unearthed cultural relics.")
        print("During an archaeology,you and your archaeological team are infatuated and trapped in this forest.")
        print("In the evening, you guys still can't find the way out.As night falls, heavy fog rises in the forest.")
        print("You can't see each other clearly, and for To keep warm, everyone had to huddle together.")
        print("When it got light, you planned to continue on your way, but when you got up the next day, you found that everyone was gone.")
        print("When you wake up in the forest,you are into the Forest World!")
        print("Your companions have also entered different worlds, and it is up to each of them to decide what secrets are hidden in them? This will be undone by you! Your first task is to solve the problem and get out of this forest alive!")

        


    #functions
def scenario1():
        
        
        
        GOOD_COMMENTS=["Smart","luckey","great"]
        BAD_COMMENTS=["sorry,go replay","sorry,you are die"]


        print("Morning!Welcome to the Forest World!")
        print("Warm tips: Pat your own face to keep yourself awake and alert, danger is everywhere in the forest, don't die because of your careless actions")
        print("You are the warrior chosen by the King of the Forest, and I am the messenger of this forest world, you cannot see me, but you can hear my voice, I will help you read the questions, and I will remind you of some of the more detailed details of the questions, so that you will not die so soon")
        print("Good luck!")

        print("Ok.")
        print("Now,you have two options:1,walk into the deeper forest(go walk front)2,get killed by the system.")
        print("Please listen the question careful,give the system your best answer,thank you.")

        
        
        
        QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{} "
        question = "Do you want to front/into the deeper forest? ?"
        a= "Yes,i want to"
        b= "No,nononono"
        c= "into the deeper forest/go walk front"
        d= "get killed by the system"

        answer= input(QUESTION_FORMAT.format(question,a,b,c,d)).lower()
        
        if answer == "a"or"c".lower() or answer==a or c.lower():

            print(GOOD_COMMENTS[2]) 
                    
        elif answer =="":
            print("not sure???") 
            print(BAD_COMMENTS[1])
        else:
            print("you are die sorry")
            print(BAD_COMMENTS[1])
        
        
    #functions

def dieofstrvation():
        
            
    print("Sorry you are dead")

    answer=input("Do you want to play this game again?")

    if answer =="yes":
         print("just open this game again and replay")

<<<<<<< HEAD
=======
#main code
intro()
scenario1()
dieofstrvation()
>>>>>>> 56fafebd075a278701cec54004ef9e29233b8afb

#------------------------------------------Tixha
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
       
    


    
    
=======
#------------------------------------------------Annas________________
# set up variables to control how game flows
gameflow = "start"

# mock waiting for Tixha code for scenario 3
weapon = "sword"

def scenario6():
    print (".")
    print (".")
    print (".")
    print ("Congratulations you have defeated the monster!")
    print ("You have finished forest escape game.")
    gameflow = "success"

def scenario7():
     print (".")
     print (".")
     print (".")
     print ("You wander deeper into the forest.")

# scenario5 ():

while True:
        print("You hear bushes rusling and go to investigate it. You come across a monster and it sees you - what do you do?")
        scenario5choice = input ("Do you want to fight the monster?")
        print (gameflow)
        if scenario5choice == "yes":
            print("You fight the monster")
            if weapon == "sword":
                scenario6()
            elif weapon != "sword":
                print ("The monster defeats you and you die!")
                break
        else:
            print("You move on further down the path")
            scenario7()
        if gameflow == "success":
             break




>>>>>>> Stashed changes
