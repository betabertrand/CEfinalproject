#final project

#guessing race

#def turtleracesetup():
   

    

menuchoice = 5



def randomfunc(x):      #function for random number 
    import random
    number = random.randrange(x) + 1
    return number

random1 = randomfunc(3)
random2 = randomfunc(3)
random3 = randomfunc(3)
random4 = randomfunc(3)
random5 = randomfunc(3)
random6 = randomfunc(3)
random7 = randomfunc(3)
random8 = randomfunc(3)
random9 = randomfunc(3)
random10 = randomfunc(3)

guess1 = 0
guess2 = 0
guess3 = 0
guess4 = 0
guess5 = 0
guess6 = 0
guess7 = 0
guess8 = 0
guess9 = 0
guess10 = 0


print("Menu:\n1)Guessing Race\n2)Exit\n")

while menuchoice > 2 or menuchoice < 0:

    menuchoice = int(input("\nPlease enter your menu choice: "))

    if menuchoice == 1:
        import turtle
        t=turtle.Pen()
        t.up()
        t.backward(250)
        t.left(90)
        t.forward(25)
        t.left(180)
        t.down()
        t.forward(5)
        t.up()
        t.forward(5)
        t.down()
        t.forward(5)
        t.up()
        t.forward(5)
        t.down()
        t.forward(5)
        t.up()
        t.forward(5)
        t.down()
        t.forward(5)
        t.up()
        t.forward(5)
        t.down()
        t.forward(5)
        t.up()
        t.forward(5)
        t.left(90)
        t.down()
        t.forward(500)
        t.up()
        t.left(90)
        t.forward(50)
        t.left(180)
        t.down()
        t.forward(5)
        t.up()
        t.forward(5)
        t.down()
        t.forward(5)
        t.up()
        t.forward(5)
        t.down()
        t.forward(5)
        t.up()
        t.forward(5)
        t.down()
        t.forward(5)
        t.up()
        t.forward(5)
        t.down()
        t.forward(5)
        t.up()
        t.forward(5)
        t.backward(50)
        t.right(90)
        t.down()
        t.forward(500)
        t.up()
        t.left(90)
        t.forward(25)
        t.left(90)
        t.down()

        print("Welcome to the Guessing Race!!!")

        #Print Rules
        print("This is the Guessing Race where you must face different opponets to reach the finish line. If you choose the same number as your opponent, then you advance and after you beat all the opponents you will reach the finish line")
              
        #call turtleracesetup
        #turtleracesetup()
        
        
        print("1)Rock\t2)Paper\t3)Scissors")

        guess1 = int(input("Choose your weapon: "))
        print("Opponent: %s" % random1)

        if guess1 == random1:
                     print("You've beaten your oppponent, you get to advance!")
                     t.forward(50)
                     print("1)Rock\t2)Paper\t3)Scissors")
                     
                     guess2 = int(input("Choose your next weapon: "))
                     print("Opponent: %s" % random2)

                     

                     if guess2 == random2:
                            print("You've beaten your oppponent, you get to advance!")
                            t.forward(50)
                            print("1)Rock\t2)Paper\t3)Scissors")
                            guess3 = int(input("Choose your next weapon: "))
                            print("Opponent: %s" % random3)

                            

                            if guess3 == random3:
                                 print("You've beaten your oppponent, you get to advance!")
                                 t.forward(50)
                                 print("1)Rock\t2)Paper\t3)Scissors")
                                 guess4 = int(input("Choose your next weapon: "))

                                 print("Opponent: %s" % random4)    



                                 if guess4 == random4:
                                        print("You've beaten your oppponent, you get to advance!")
                                        t.forward(50)
                                        print("1)Rock\t2)Paper\t3)Scissors")
                                        guess5 = int(input("Choose your next weapon: "))
                                        print("Opponent: %s" % random5)

                                    

                                        if guess5 == random5:
                                             print("You've beaten your oppponent, you get to advance!")
                                             t.forward(50)
                                             print("1)Rock\t2)Paper\t3)Scissors")
                                             guess6 = int(input("Choose your next weapon: "))
                                             print("Opponent: %s" % random6)

                                             
                                    
                                             if guess6 == random6:
                                                 print("You've beaten your oppponent, you get to advance!")
                                                 t.forward(50)
                                                 print("1)Rock\t2)Paper\t3)Scissors")
                                                 guess7 = int(input("Choose your next weapon: "))
                                                 print("Opponent: %s" % random7)
                                                      
                                                 

                                                 if guess7 == random7:
                                                    print("You've beaten your oppponent, you get to advance!")
                                                    t.forward(50)
                                                    print("1)Rock\t2)Paper\t3)Scissors")
                                                    guess8 = int(input("Choose your next weapon: "))
                                                    print("Opponent: %s" % random8)

                                                    

                                                    if guess8 == random8:
                                                         print("You've beaten your oppponent, you get to advance!")
                                                         t.forward(50)
                                                         print("1)Rock\t2)Paper\t3)Scissors")
                                                         guess9 = int(input("Choose your next weapon: "))
                                                         print("Opponent: %s" % random9)
                                                    

                                                         

                                                         if guess9 == random9:
                                                                print("You've beaten your oppponent, you get to advance!")
                                                                t.forward(50)
                                                                print("1)Rock\t2)Paper\t3)Scissors")
                                                                guess10 = int(input("Choose your next weapon: "))
                                                                print("Opponent: %s" % random10)

                                                                
                                                                                                                                
                                                                if guess10 == random10:
                                                                     print("You've beaten your oppponent, you get to advance!")
                                                                     t.forward(75)
                                                                     print("\nYOU WON THE RACE!! CONGRADULATIONS!!!!!!!!")
                                                                     

            

                                                        
        else:
                    print("You lose....")

    else:
        print("Good Bye.")
                                             
                     

                         
        

            
                        

        
