c = 1



while c < 101:
    if c % 15 == 0:
        print("fizzbuzz")
    elif c % 3 == 0:
        print("fizz")
    elif c % 5 == 0:
        print("buzz")
    else:
        print(c)



    c += 1
    