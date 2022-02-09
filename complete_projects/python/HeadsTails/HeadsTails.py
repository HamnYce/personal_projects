from random import randint
i = 0
num = int(input("how many times would you like to repeat head or tails?\n"))
while i < num:
    headstails = randint(0,1)
    if headstails == 0:
        print("Heads")
    else:
        print("Tails")
    i += 1