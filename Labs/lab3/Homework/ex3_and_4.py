from turtle import *
def draw_square(length , color):
    pencolor(color)

    for i in range(4):
        forward(length)
        left(90)
    
speed(0)
pensize(2)
shape("turtle")
# draw_square(100, 'blue')

for i in range(30):
        draw_square(i * 5, 'red')
        left(17)
        penup()
        forward(i * 2)
        pendown()
        
mainloop()