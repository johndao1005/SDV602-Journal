"""
An adventure game which allow the users to make choice in order to escape a lighthouse
First users will wake up in a room
    Then try to open the door with key in pocket or ram the door => broken arms
        Stair broken 
            search the room again or try to jump => die
                using rope to go down slowly 
                    go bottom floor then reach dead end but found a knife 
                        =>kill or die if die then wake up in the room
            
Choose to jump out of window then either reloop or die
"""

def lighthouseRoom():
    isMonster = False
    if isMonster == False:
        firstchoice =input("Welcome To the lighthouse,\n You just wake up to find yourself in a cold room with nothing\n\
                        but darkness around, outside only the sound of the ocean and cold gale while you \n\
                        lying on the, cold dirty floor. Suddenly loud noise can be hear outside. Looking out the window,\n\
                        you saw a dark shadow with claw climb up the light house.\n\
                        What do you want to do?(just type the number of your choise or Y, N)\n\
                        1.jump out\n\
                        2.try to escape")
        if firstchoice =='2':
                thirdchoice = input("Looking at the door tightly locked door. What would you do?\n\
                                    1. look for key(taking too long)\n\
                                    2. just ram the door(might hurt a bit\n)")
                if thirdchoice =="1":
                    fourthchoice = input("Lucky the key is in your pocket somehow. You unlock the door and want to go down the stair but\n\
                                    The stair is broken. What do you do? \n\
                                    1. running back to find a rope\n\
                                    2. trying to jump down\n")
                    if fourthchoice == '1':
                        fifthchoice = input('Running back you facing the monster. there is a sword nearby\n\
                                            Would you take the sword and fight for your last chance? Y or N')
                        if fifthchoice == 'n':
                            lastchoice = input("Taking the sword and fight for your life. Surpisingly, you seem to know\n\
                                                The monster movement like yourself and you win after stabing it heart. Upon\n\
                                                coming closer and remove the mask, you saw your face smiling in relieve. \n\
                                                Looking at the mask, look like it is pulling you over. With the mask inching \n\
                                                Closer to your face. Would you accpet it? Y or N")
                            if lastchoice == "y":
                                    isMonster = True
                                    lighthouseRoom()
                            else:
                                    print('Understanding everything just a loop. You stab your heart with other hand.')
                        else:
                            print("Too scared from looking at the monster. You begged for your life. Seem like u didnt watch much\n\
                                scary movie, why begging then you will die anyway num num. Dont need to say much, You die\n")
                            lighthouseRoom() if input("\ndo you want to restart? Y or N\n") == 'y' else False
                    else:
                        print("you over jump and hurt your leg. The Monster catch up quickly and you die. lol \n")
                        lighthouseRoom() if input("\ndo you want to restart? Y or N\n") == 'y' else False
                else:
                    print("You dislocate your shouder and try to look for key instead. but the monster catch up\n\
                            So you die. Too bad.")
                    lighthouseRoom() if input("\ndo you want to restart? Y or N\n") == 'y' else False
                    
        else:
                secondchoice = input("You jump out the window and try to grab the Monster to die with you.\
                            When both of you are falling, you remove the mask to see yourself with a happy smile,\
                            The monster whisper in your ear: \n'Wear the mask if you want something new'\n\
                            Do you want to wear the mask? Y or N")
                if secondchoice== "y":
                    isMonster = True
                    lighthouseRoom()
                elif secondchoice == "n":
                    print("Waking up in your room feeling unreal but relieved. Suddenly, you Feel tired and want to go back to sleep.\n\
                    Would you sleep again my little Lamb?")
                    lighthouseRoom() if input("\ndo you want to restart? Y or N\n") == 'y' else False
    else:
        print("The Monster is inside you and you are the monster, You will keep hunting till you die or save yourself")
        return False
if __name__ == '__main__':
    lighthouseRoom()