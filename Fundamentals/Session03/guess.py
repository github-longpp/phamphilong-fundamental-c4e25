from random import *
rd = randint(1, 100)
loop = True

while loop:
    n = int(input("Enter your number: "))
    loop = False
    if n < rd:
        loop = True
        print("Smaller")
    if n > rd:
        loop = True
        print("Bigger")
        
print("Bingo!!")