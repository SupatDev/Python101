import turtle
#t = turtle.Turtle()
turtle.bgcolor('white')

def form_sq(side):
    for i in range(4):
        my_pen.fd(side)
        my_pen.left(90)
        side -= 5
        
my_pen = turtle.Turtle()
my_pen.color('blue')

tut = turtle.Screen()

side = 200

for i in range(10):
    form_sq(side)
    side -= 20
