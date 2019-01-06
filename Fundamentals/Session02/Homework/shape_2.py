from turtle import *
pensize(2)
pencolor("red")
speed(0)
shape("turtle")
a = 3
for j in range(a,7):
    for i in range(a):
        if(a % 2 == 1):
            pencolor("blue")
        else:
            pencolor("red")    
        b = (1 - 2/a) * 180
        fd(100)
        left(180 - b)
    a += 1



mainloop()