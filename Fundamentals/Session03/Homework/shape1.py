from turtle import *
pensize(2)
pen_list = ["red" , "blue" , "brown" , "yellow" , "silver"]
speed(0)
shape("turtle")
a = 3
for j in range(a,8):
    for i in range(a):
        pencolor(pen_list[a - 3])
        b = (1 - 2/a) * 180
        fd(100)
        left(180 - b)
    a += 1



mainloop()