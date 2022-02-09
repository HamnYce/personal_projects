from random import randint


i = 0;
num = 50
print("press enter at any point to keep going or input 0 to exit out of the application")
while i < 1:
    x = 0
    x = int(input())
    
    num2 = randint(1,100)
    if x < 1:
       i = 2
    else x >= 1:
       if num > num2:
           print("Lower")
       elif num < num2:
           print("higher")