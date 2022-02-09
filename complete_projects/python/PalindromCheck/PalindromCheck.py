#palindrom



#0:-1 , 1:-2 , 2:-3, 3:-4, the index of the other side is (x+1)*-1

print("please input a string to see if it is a palindrom")
sting = input()
wordlen = len(sting)


tr = 0
fa = 0
c = 0


while c < wordlen:
    if (sting[c] == sting[ ( (c+1)*-1) ]):
        tr += 1
    else:
        fa += 1
    c += 1


if tr >= wordlen:
    print("this is a palindrom")
elif fa > 1:
    print("this is not a palindrom")
else:
    print("else")
    print("this is not a palindrom")

    






