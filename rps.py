import random
options=['Rock','Paper','Scissor']
name=input("Enter your name :")
ComputerScore=0 
PlayerScore=0
NumberOfRounds=0
gameOn=True
print(f"Welcome {name.title()}\n")
z=int(input("Enter your game mode:\n1: Win on 3 points\n2: Number of rounds\nChoose (1/2):"))


if z==1:
    while PlayerScore!=3 or ComputerScore!=3:
        ComputerOption=random.choice(options)
        PlayerOption=input("Enter Rock/ Paper/ Scissor :").title()
        print(f"Computer option :{ComputerOption}")
        print(f"{name.title()} option :{PlayerOption}")
        NumberOfRounds += 1
        if ComputerOption==PlayerOption:
            print('Tie')
        elif (ComputerOption=='Rock' and PlayerOption == 'Scissor') or (ComputerOption=='Scissor' and PlayerOption=='Paper') or (ComputerOption=='Paper' and PlayerOption=='Rock'):
            print("Computer wins")
            ComputerScore += 1
        elif (PlayerOption=='Rock' and ComputerOption == 'Scissor') or (PlayerOption=='Scissor' and ComputerOption=='Paper') or (PlayerOption=='Paper' and ComputerOption=='Rock'):
            print(f"{name.title()} wins")
            PlayerScore += 1
        else:
            print("Choose a valid option to play this game.") 
        print("\n-------------------------")
        print("")
        print(f"Round No: {NumberOfRounds}")
        print("------ Score Board ------")
        print(f"{name.title()}: {PlayerScore} | Computer: {ComputerScore}")
        print("===============================")
        print("")
        if PlayerScore==3 or ComputerScore==3:
            gameOn=False
            break
    if PlayerScore==ComputerScore:
        print("Draw!!")
    elif PlayerScore>ComputerScore:
        print(f"Congrats {name.title()}, You won the game!!")
    else:
        print(f"Oops Computer won the game!! Better luck next time {name.title()}!")


if z==2:
    no_round=int(input("\nEnter number of rounds you want to play: "))
    while NumberOfRounds<no_round:
        ComputerOption=random.choice(options)
        PlayerOption=input("Enter Rock/ Paper/ Scissor :").title()
        print(f"Computer option :{ComputerOption}")
        print(f"{name.title()} option :{PlayerOption}")
        NumberOfRounds += 1
        if ComputerOption==PlayerOption:
            print('Tie')
        elif (ComputerOption=='Rock' and PlayerOption == 'Scissor') or (ComputerOption=='Scissor' and PlayerOption=='Paper') or (ComputerOption=='Paper' and PlayerOption=='Rock'):
            print("Computer wins")
            ComputerScore += 1
        elif (PlayerOption=='Rock' and ComputerOption == 'Scissor') or (PlayerOption=='Scissor' and ComputerOption=='Paper') or (PlayerOption=='Paper' and ComputerOption=='Rock'):
            print(f"{name.title()} wins")
            PlayerScore += 1
        else:
            print("Choose a valid option to play this game.") 
        print("\n-------------------------")
        print("")
        print(f"Round No: {NumberOfRounds}")
        print("------ Score Board ------")
        print(f"{name.title()}: {PlayerScore} | Computer: {ComputerScore}")
        print("===============================")
        print("")
        if NumberOfRounds==no_round:
            gameOn=False
            break
    if PlayerScore==ComputerScore:
        print("Draw!!")
    elif PlayerScore>ComputerScore:
        print(f"Congrats {name.title()}, You won the game!!")
    else:
        print(f"Oops Computer won the game!! Better luck next time {name.title()}!")