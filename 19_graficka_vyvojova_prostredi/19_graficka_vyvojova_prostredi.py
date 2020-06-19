import turtle

def House(pen):
    pen.pu()
    pen.setpos(-100, 0)
    pen.pencolor('green')
    pen.pd()
    for i in range(4):
        pen.fd(200)
        pen.rt(90)
    pen.pencolor('red')
    pen.bk(10)
    for i in range(3):
        pen.fd(220)
        pen.lt(120)


if __name__ == "__main__":
    pen = turtle.Turtle()
    pen.speed(10)
    pen.pensize(5)
    House(pen)
    turtle.mainloop()




