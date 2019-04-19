import random
from random import randrange


def End():
    print("Having met your goal, you leave. You return to your home town to devote yourself to meme repopulation")
    print("At first people are skeptical and afraid of such self expression in a time of heavy cencorship")
    print("But then people slowly start to like it, like wildfire it spreads")
    print("Before mega corporations or the corrupt government can stop it, people are reeing and demanding chicken tendies across the land")
    print("5 years after this fateful day, meme reserve parks are built to consolidate efforts to preserve memes for future generations to enjoy")
    print("As chaotic as it may be, the people are happy and our hero is renowned as a saint")
    input("THE END")

def TrueEnd():
    print("Before you can grasp the handle, the door swings open, you walk forward.")
    print("Entering the new room, you come across a dude")
    print("Look at this dude")
    print("What a dude")
    PlayerFeedback = input("Yo its ya boy Jake, the creator of this game, you like it? (1)[LIKE] (2)[DISLIKE]")

    Valid = ("1","2")
    while PlayerFeedback not in Valid:
        PlayerFeedback = input("Not a valid choice try again m8")

    if PlayerFeedback == "1" or "2":
        print("Lol tell me irl you spaz")
        print("All memeing aside, thank you for playing this game and getting this far. Please do give me feedback so I can make better games in the future")
        print("Hopefully you had as much fun playing this game as I did making it ;P")
        input("THE TRUE ENDING")
    
def Room1():
    print("""You open the door. This room seems rather clean considering this house has been abandonded
          since the year 19XX. Within it is a desk, a chair and a note on the desk which has the number 3 on it.""")
    StayOrLeave=input("Do you wish to stay or leave the room? (1)[Stay] (2)[Leave]")

    Valid = ("1","2")
    while StayOrLeave not in Valid:
        StayOrLeave = input("Not a valid choice try again m8")
        
    if StayOrLeave == "2":
        print("You return to the main room")
        Hub()

    if StayOrLeave == "1":
        print("You stay in the room a bit longer")
        StayOrLeave2=input("Do you wish to stay or leave the room? (1)[Stay] (2)[Leave]")

        Valid = ("1","2")
        while StayOrLeave2 not in Valid:
            StayOrLeave2 = input("Not a valid choice try again m8")

        if StayOrLeave2 == "2":
            print("You return to the main room")
            Hub()

        if StayOrLeave2 == "1":
            print("You stay in the room for even longer.")
            StayOrLeave3=input("Do you wish to stay or leave the room? (1)[Stay] (2)[Leave]")

            Valid = ("1","2")
            while StayOrLeave3 not in Valid:
                StayOrLeave3 = input("Not a valid choice try again m8")

            if StayOrLeave3 == "2":
                print("You return to the main room")
                Hub()

            if StayOrLeave3 == "1":
                print("""At this point the players obsession with the bland starter room bordered on creepy
                       and reflected poorly on their overall personality""")
                StayOrLeave4=input("Do you wish to stay or LEAVE THE ROOM? (1)[Stay] (2)[Leave]")

                Valid = ("1","2")
                while StayOrLeave4 not in Valid:
                    StayOrLeave4 = input("Not a valid choice try again m8")

                if StayOrLeave4 == "2":
                    print("You finally return to the main room")
                    Hub()

                if StayOrLeave4 == "1":
                    print("""You try to stay in this bland room for as long as possible but the overwhelming
                          urge to progress the game clutches at your soul and you leave the room""")
                    Hub()
    

def Room2():
    ActualCup=randrange(1, 3)
    print("""You open the door. This room has minimal dust in it, inside is a chest with a lock in the middle
          of the room. Behind it are 3 cups that are magically shifting around.""")
    CupChoice=int(input("Do you pick the left cup, the middle cup or the right cup? [1] [2] [3]"))

    while CupChoice != ActualCup:
        CupChoice=int(input("You lift the cup to reveal nothing. You set it back down in defeat. Guess again lol. [1] [2] [3]"))

    if CupChoice == ActualCup:
        print("You lift the cup to reveal a key. You use it to unlock the chest and inside is the number 2 carved into the back.")
        print("You return to the main room")
        Hub()

def Room3():
    RiddleAnswer = input("""You open the door. Dust falls off the door and onto you which you quickly brush off. You notice a sign
                    which reads: I am seven letters long, if you eat me you will die. What am I? (one word starts with a capital letter)""")
    while RiddleAnswer != "Nothing":
        RiddleAnswer = input("It seemed that NO THING you did had any effect.")
    print("The number 6 appears. You don't bother to question the physics or the lazy writing of this and swiftly move on.")
    print ("You return to the main room")
    Hub()

def Room4():
    print("""You see a small imp covered in flames. He doesn't seem hurt by them. Above him is a sign that says 'Mini Boss',
          he catches you looking at the sign and says:""")
    print("That's an attempt at humour from the creator")
    FightOrTalk = input("Anyway, we're supposed to fight so let's get started. (1)[Fight] (2)[Talk]")

    Valid = ("1","2")
    while FightOrTalk not in Valid:
        FightOrTalk = input("Not a valid choice try again m8")
        
    if FightOrTalk == "2":
        print("""You deliver a passionate speech about friendship and comradery. Overcome with emotions, the small flame imp
              falls to his knees and weeps uncontrollably and cries out:""")
        print("You've given me a lot to think about, the answer you seek is 7, go forth and save the world, Gnash!")
        Hub()

    if FightOrTalk == "1":
        print("You pull out a bottle of water and splash him real good. He seems visibly traumatised and says:")
        FinishOrSpare = input("OOF that actually hurts quite a bit (1)[FINISH HIM] (2)[SPARE HIM]")

        Valid = ("1","2")
        while FinishOrSpare not in Valid:
            FinishOrSpare = input("Not a valid choice try again m8")

        if FinishOrSpare == "1":
            print("""You unholster your trusty machine pistols and pop many, many caps in his ass. You strike various poses whilst
                   keeping the guns pointed at him and firing. His body is more holes than body at this point. The holes are in the shape
                   of the number 7. Good job, you must be very proud of yourself""")
            Hub()

        if FinishOrSpare == "2":
            print("""You realise the strongest power in the universe is the power of friendship and that todays enemies can be
                  tomorrows friends. You spare him and he tells you the answer you seek is 7""")
            Hub()

def Room5():
    TakeOrFix = input("""You look around the room and notice a sign that says 'DO NO ENTER WIP'. Looking around some more you notice
                      a broken dispenser, some frayed wires, a button and a note. (1)[TAKE NOTE] (2)[FIX PUZZLE]""")
    Valid = ("1","2")
    while TakeOrFix not in Valid:
        TakeOrFix = input("Not a valid choice try again m8")

    if TakeOrFix == "1":
        print("""Wanting to compromise the integrity of the game, you take the note and read the number 4, without fixing the puzzle
              and earning it. Bad player, your actions here won't be forgotten.""")
        Hub()

    if TakeOrFix == "2":
        print("""Not wanting to comrpomise the integrity of the game, you repair the puzzle and solve it, obtaining the note fair and sqaure,
                reading the number 4. Good job player, your actions here won't be forgotten.""")
        Hub()

def Room6():
    PressOrNoPress = input("""You enter the room. It's a room with blandness that could rival the first room, except there is a podium
                           with a singular red button in the middle of the room. (1)[Press] (2)[Don't Press]""")
    Valid = ("1","2")
    while PressOrNoPress not in Valid:
        PressOrNoPress = input("Not a valid choice try again m8")

    while PressOrNoPress == "2":
        PressOrNoPress = input("""As much of a cool guy you are, rushing in and making an uninformed decision which could potentially be
                               life changing is not a very cool thing to do. You decide to play it safe and ponder the meaning of the button some more.
                               [Press] [Don't Press]""")

    if PressOrNoPress == "1":
        print("""You nervously approach the button. You press down with all your might AND THEN SUDDENLY! The button pops out, falling onto the floor
              . On the inside is the number 8""")
        print("You return to the main room")
        Hub()

def Room7():
    print("""You exit the main room. ehh you see what I did there? Anyway, in this room is a regular sized water imp. You're unsure how you know
          what constitutes as regular sized for an imp but you move on from that thought.""")
    FightOrRoast = input("Finna square up boi. (1)[Fight] (2)[ROAST]")

    Valid = ("1","2")
    while FightOrRoast not in Valid:
        FightOrRoast = input("Not a valid choice try again m8")
        
    if FightOrRoast == "1":
        print("""You rush him immediatly, picking him up and using the forward momentum to yeet him out the window behind him.
        You never hear him hit the ground and you're unsure you want to look outside.""")
        print("A piece of paper appears to have fallen out of his pocket, you pick it up and read the number 1 on it.")
        Hub()

    if FightOrRoast == "2":
        print("""You put your hands together and inhale deeply. The water imp is confused as to what you're doing, little does he know
              the carnage you're about to unleash. You point your hands upwards, then snap them towards him and exclaim:""")
        print("B O I!")
        print("The imp is blown back onto the floor. It appears your roast was super effective and he is now unconscious.")
        print("A piece of paper sticks out of his pocket, you take it and see the number 1 on it.")
        Hub()

def Room8():
    ActualCode = "3267481"
    InputtedCode = input("You arrive at a pair of doors. On the right handside is a keypad with 7 X's on the display, it seems a code is required to unlock it. Have a go or type [Leave].")

    if InputtedCode == "Leave":
            Hub()

    while InputtedCode != ActualCode:
        InputtedCode = input("The display flashes red and resets. Try again or type [Leave] to go back.")

        if InputtedCode == "Leave":
            Hub()

    if InputtedCode == ActualCode:
        print("The display flashes green and you hear a click. The doors swing open to reveal ever extending darkness")
        print("You enter the room. You feel like you have no choice. A point of no return if you will...")
        print("You quickly realise the ever extending darkness you saw was actually a black curtain over the dooorway")
        print("You walk throught it")
        print("A tall flame imp wearing a trench coat with a surprisingly small face stands before you")
        EXPOSEHIM = input("You feel like you know where this is going... (1)[EXPOSE HIM]")

        if EXPOSEHIM == "1":
            print("You rush him and pull off the trench coat. It's 3 small flame imps stacked on top of each other!")
            print("You said this would work! the one on the bottom cries out")
            print("Might work the one in the middle replies")
            print("To be fair the view is pretty great from up here the top one gleefully adds")
            print("You brandish 3 bottles of water menacingly, hydration is important but so is defeating your enemies")
            print("NOT THAT! Okay you win just go ahead the top one says")
            print("You walk past them and in front of you stands an iron door")
            print("Next to it is a sign that reads NO RETURN")
            print("Attached is a picture of a small frog")
            print("""__________████████_____██████
_________█░░░░░░░░██_██░░░░░░█
________█░░░░░░░░░░░█░░░░░░░░░█
_______█░░░░░░░███░░░█░░░░░░░░░█
_______█░░░░███░░░███░█░░░████░█
______█░░░██░░░░░░░░███░██░░░░██
_____█░░░░░░░░░░░░░░░░░█░░░░░░░░███
____█░░░░░░░░░░░░░██████░░░░░████░░█
____█░░░░░░░░░█████░░░████░░██░░██░░█
___██░░░░░░░███░░░░░░░░░░█░░░░░░░░███
__█░░░░░░░░░░░░░░█████████░░█████████
_█░░░░░░░░░░█████_████___████_██████
_█░░░░░░░░░░█______█_███__█_____███_█
█░░░░░░░░░░░░█___████_████____██_████
░░░░░░░░░░░░░█████████░░░████████░░░█
░░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░░█
░░░░░░░░░░░░░░░░░░░░██░░░░█░░░░░░██
░░░░░░░░░░░░░░░░░░██░░░░░░░███████
░░░░░░░░░░░░░░░░██░░░░░░░░░░█░░░░░█
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
░░░░░░░░░░░█████████░░░░░░░░░░░░░░██
░░░░░░░░░░█▒▒▒▒▒▒▒▒███████████████▒▒█
░░░░░░░░░█▒▒███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░░░░░░░░█▒▒▒▒▒▒▒▒▒█████████████████
░░░░░░░░░░████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░░░░░░░░░░░░░░░░░██████████████████
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
██░░░░░░░░░░░░░░░░░░░░░░░░░░░██
▓██░░░░░░░░░░░░░░░░░░░░░░░░██
▓▓▓███░░░░░░░░░░░░░░░░░░░░█
▓▓▓▓▓▓███░░░░░░░░░░░░░░░██
▓▓▓▓▓▓▓▓▓███████████████▓▓█
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█""")
            print("""You take the picture and something about it captivates you. Unable to put it into words but wanting to preserve this for future generations
                  you quickly stuff it into your pocket and vow to spread this picture far and wide for all to see""")
            print("Returning your focus to the door. You have what you came for but can still go further")
            FinalChoice = input("This is the real point of no return. Are you ready? (1)[LEAVE] (2)[ENTER]")

            Valid = ("1","2")
            while FinalChoice not in Valid:
                FinalChoice = input("Not a valid choice try again m8")

            if FinalChoice == "1":
                End()

            if FinalChoice == "2":
                TrueEnd()
        
def Hub():
    print("Gnash opens the door, his eyes underneath his radical shades surveying the room.")
    RoomChoice=input("""8 doors can be seen around the mansion, each with a number above the door, which do you enter?
          (1) (2) (3) (4) (5) (6) (7) (8) """)

    Valid = ("1","2","3","4","5","6","7","8")
    while RoomChoice not in Valid:
        RoomChoice = input("Not a valid choice try again m8")

    if RoomChoice == ("1"):
            Room1()

    if RoomChoice == ("2"):
            Room2()

    if RoomChoice == ("3"):
            Room3()

    if RoomChoice == ("4"):
            Room4()

    if RoomChoice == ("5"):
            Room5()

    if RoomChoice == ("6"):
            Room6()

    if RoomChoice == ("7"):
            Room7()

    if RoomChoice == ("8"):
            Room8()
        
print("""The year is 20XX. Memes have been outlawed and gone extinct, or so
        we thought. An urban myth details of the last pepe hidden
        in an old mansion. Our hero, Gnash 'Cool guy' Renegade has set off to
        recover the last meme.""")
Enter=input("Do you wish to enter? (1)[YES](2)[NO]")

Valid = ("1","2")
while Enter not in Valid:
        Enter = input("Not a valid choice try again m8")

if Enter == "2":
    print("""Before our hero could reach the door, he is stricken with a critical
            illness known as normie, he is unable to enter the mansion feelsbadman""")
    input("You got the bad ending :(")

if Enter == "1":
    Hub()
