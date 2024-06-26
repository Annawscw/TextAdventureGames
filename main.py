#functions



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

    

    
    
    print("You are a very famous researcher of unearthed cultural relics.During an archaeology,you and your archaeological team are infatuated and trapped in this forest.In the evening, you guys still can't find the way out.As night falls, heavy fog rises in the forest. You can't see each other clearly, and for To keep warm, everyone had to huddle together. When it got light, you planned to continue on your way, but when you got up the next day, you found that everyone was gone.")
    print("When you wake up in the forest,you are into the Forest World!")
    print("Your companions have also entered different worlds, and it is up to each of them to decide what secrets are hidden in them? This will be undone by you! Your first task is to solve the problem and get out of this forest alive!")

    


#functions
def scenario1():
    
    print("Morning!Welcome to the Forest World!")
    print("You are the warrior chosen by the King of the Forest, and I am the messenger of this forest world, you cannot see me, but you can hear my voice, I will help you read the questions, and I will remind you of some of the more detailed details of the questions, so that you will not die so soon")
    print("Good luck!")

#functions

def dieofstrvation():
      pass

#main code

intro()


    
