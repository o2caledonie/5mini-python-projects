text=str(input('Write a string of characters: '))

def accro_generator(string):
    words = string.split()
    accro = ''
    for i in words:
        accro = accro + str(i[0]).upper()
    return accro

result=accro_generator(text)

print(f"Here is the accronyme : {result}")