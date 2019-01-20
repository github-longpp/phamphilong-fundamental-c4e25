from random import randint, choice
import calc

a = randint(1, 10)
b = randint(1, 10)
error = randint(-1,1)
op = ["+" , "-" , "*" , "/" , "%"]
pt = choice(op)
r = calc.eval(a, b , pt) + error

print(a , pt , b , "=" , r)

user_input = input("Your answer (Y/N)").upper()

result = ""

if error == 0:
    result = "Y"
    if user_input == result:
        print("Yay")
    else:
        print("Nay")
else:
    result = "N"
    if user_input == result:
        print("Yay")
    else:
        print("Nay")
    


