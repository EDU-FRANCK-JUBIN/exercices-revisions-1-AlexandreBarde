import turtle

toto = turtle.Turtle()


def square_1():
    toto.color("black")
    for i in range(4):
        toto.forward(80)
        toto.left(90)


def little_square():
    toto.forward(20)
    toto.color("red")
    toto.left(90)
    toto.forward(40)
    for i in range(2):
        toto.right(90)
        toto.forward(40)

def reset():
    toto.color("black")
    toto.home()
    toto.left(90)
    toto.forward(80)
    toto.right(90)
    toto.forward(80)

def last():
    toto.color("green")
    toto.left(120)
    toto.forward(80)
    toto.left(120)
    toto.forward(80)
    turtle.done()

square_1()
toto.home()
little_square()
reset()
last()



