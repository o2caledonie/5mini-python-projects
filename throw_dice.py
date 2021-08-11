import random
print("1: Throw dice 0: Exit")
while True:
    # We ask user to press a button
    x=int(input("Press a button "))
    if x==0:
        print('Bye, see you !')
        break
    elif x==1:
        print(random.randint(1,6))
    else:
        print("I don't understand")