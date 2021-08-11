import random
choices=['R','P','S']
score_computer=0
score_player=0

while True:
    computer = random.choice(choices)
    player = str(input('R: Rock, P:Paper or S: Scissors ? To exit press Z : ')).capitalize()
    if player==computer:
        print("Equality !")
    elif player=='R':
        if computer=='P':
            print('Sorry, you loose ! The paper covers the rock !')
            score_computer += 1
        elif computer=='S':
            print('Well done ! You win ! The rock breaks the scissors !')
            score_player += 1
    elif player=='P':
        if computer=='R':
            print('Well done ! You win ! The paper covers the rock !')
            score_player += 1
        elif computer == 'S':
            print('Sorry, you loose ! The scissors cut the paper !')
            score_computer += 1
    elif player=='S':
        if computer=='R':
            print('Sorry, you loose ! The rock breaks the scissors !')
            score_computer += 1
        elif computer == 'P':
            print('Well done ! You win ! The scissors cut the paper !')
            score_player += 1
    elif player=='Z':
        print("results : ")
        print(f"COMPUTER : {score_computer}")
        print(f"PLAYER : {score_player}")
        break
    else:
        print("I don't understand, check your answer")


