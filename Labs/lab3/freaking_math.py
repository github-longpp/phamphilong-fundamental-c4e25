from random import randint
loop = True
while loop:
    a = randint(1, 10)
    b = randint(1, 10)
    error = randint(-1,1)
    c = a + b + error
    result = a + b
    print(a , "+" , b , "=" , c)
    ans = input("Answer (y/n)")
    if result == c:
        dap_an = "y"
    else:
        dap_an = "n"
    if ans == dap_an:
        print("Yay")
    else:
        print("Nay")