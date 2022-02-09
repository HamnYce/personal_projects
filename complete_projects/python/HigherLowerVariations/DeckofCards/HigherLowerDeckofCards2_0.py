from random import randint, random
f = 1
c = 1
#create deck of cards with program instead of inputting the code one by one
#1 = clubs, 2 = hearts, 3 = diamonds, 4 = spades
#if statements where it appends depending on f i.e. f = 0 means it appends on
#clubs and having a specific list for each suit
#can help with printing out the specific card from the deck e.g. 5 of Hearts

#initing the lists for the suits
hearts = []
diamonds = []
spades = []
clubs = []

def higherLowerFunc():
    
    if newnum > num:
        print("higher")
    elif newnum < num:
        print("lower")
    else:
        print("same")
    
    

def printCard():
    if card == 11:
        print("Ace of diamonds")
    else:
        print(card,"of diamonds")

DofCards = [hearts,diamonds,spades,clubs]

while f < 5:
    c = 2
    
    if f == 1:
         while c < 12:
            diamonds.append(c)
            c+=1

    elif f == 2:
        while c < 12:
            hearts.append(c)
            c+=1

    elif f == 3:
        while c < 12:
            clubs.append(c)
            c+=1

    elif f == 4:
        while c < 12:
            spades.append(c)
            c+=1
    f += 1


########

deckSize = 40
diamondLeft = 10
spadeLeft = 10
heartLeft = 10
clubLeft = 10
num = 0
newnum = 0


while deckSize > 0 :


    randlist = randint(0,3)
    if randlist == 0 and diamondLeft > 0:
        diamondAmount = (len(diamonds)-1)
        randomCard = randint(0,diamondAmount)
        card = diamonds[randomCard]
        diamonds.pop(randomCard)
        diamondLeft -= 1
        deckSize -= 1
        printCard()
        newnum = card
        higherLowerFunc()
        num = card
        input()


    elif randlist == 1 and heartLeft > 0:
        heartAmount = (len(hearts)-1)
        randomCard = randint(0,heartAmount)
        card = hearts[randomCard]
        hearts.pop(randomCard)
        heartLeft -= 1
        deckSize -= 1
        printCard()
        newnum = card
        higherLowerFunc()
        num = card
        input()


    elif randlist == 2 and spadeLeft > 0:
        spadeAmount = (len(spades)-1)
        randomCard = randint(0,spadeAmount)
        card = spades[randomCard]
        spades.pop(randomCard)
        spadeLeft -= 1
        deckSize -= 1
        printCard()
        newnum = card
        higherLowerFunc()
        num = card
        input()


    elif randlist == 3 and clubLeft > 0:
        clubAmount = (len(clubs)-1)
        randomCard = randint(0,clubAmount)
        card = clubs[randomCard]
        clubs.pop(randomCard)
        clubLeft -= 1
        deckSize -= 1
        printCard()
        newnum = card
        higherLowerFunc()
        num = card
        input()









print("the deck is empty")
