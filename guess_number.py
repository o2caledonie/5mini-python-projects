import random
number_to_guess=random.randint(1,6)
result=0
for i in range(3):
    chosen_number=int(input('Choose a number : '))
    if chosen_number==number_to_guess:
        print("Well done !")
        result=1
        break
    elif chosen_number > number_to_guess:
        print("The number you suggest is too high !")
    elif chosen_number < number_to_guess:
        print("The number you suggest is too low !")

if result==1:
    print(f"The right number is {number_to_guess}")
else:
    print(f"Game over ! Sorry, the right number was {number_to_guess}")