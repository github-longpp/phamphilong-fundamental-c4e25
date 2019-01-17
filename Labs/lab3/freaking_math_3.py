from random import randint, choice
loop = True
while loop:
    a = randint(1, 10)
    b = randint(1, 10)
    error = randint(-1,1)
    op = ["+" , "-" , "*" , "/" , "%"]
    pt = choice(op)
    if pt == "+":
        c = a + b + error
        result = a + b
    if pt == "-":
        c = a - b + error
        result = a - b
    if pt == "*":
        c = a * b + error
        result = a * b
    if pt == "/":
        c = a / b + error
        result = a / b
    if pt == "%":
        c = a % b + error
        result = a % b
    print(a , pt , b , "=" , c)
    ans = input("Answer (y/n)")
    if result == c:
        dap_an = "y"
    else:
        dap_an = "n"
    if ans == dap_an:
        print("Yay")
    else:
        print("Nay")

def op(o):
    if pt == o:
        c = a + b + error
        result = a + b