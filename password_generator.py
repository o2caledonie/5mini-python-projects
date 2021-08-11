import random
# Ask user to give password length
pwlength=int(input('Give password length: '))
# List of allowed characters
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-.:;<=>?@[]^_`{|}~"
# To group characters randomly
password="".join(random.sample(s,pwlength))
print(password)


