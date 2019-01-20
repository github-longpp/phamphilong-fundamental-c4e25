from random import *
import calc


def generate_quiz():
    x = randint(0,20)
    y = randint(0,20)
    error = randint(-1,1)
    pt = ["+","-","*","/"]
    op = choice(pt)
    result = calc.eval(x,y,op)+error
    return [x,y,op,result]
    

def check_answer(x, y, op, result, user_choice):
    right = calc.eval(x,y,op)
    check = None
    if user_choice == True:
        if right == result:
            check = True
        else :
            check = False
    if user_choice == False:
        if right != result:
            check = True
        else :
            check = False
    return check



