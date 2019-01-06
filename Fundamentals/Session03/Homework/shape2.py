from turtle import *
speed(0)
pensize(2)
pen_list = ["red" , "blue" , "brown" , "yellow" , "silver"]

for i in pen_list:
    fillcolor(i)
    pencolor(i)
    begin_fill()
    for j in range (2):
        fd(50)
        left(90)
        fd(80)
        left(90)
    fd(50)
    end_fill()
    
mainloop()