import turtle

def Snowflake(pen, generation, length):
    pen.pu()
    pen.pensize(3)
    pen.setpos(-250, 150)
    pen.pd()
    for i in range(3):
        Koch(pen, generation, length)
        pen.right(120)

def Koch(pen, generation, length):
    if generation <= 0:
        pen.fd(length)
    else:
        Koch(pen, generation - 1, length / 3)
        pen.left(60)
        Koch(pen, generation - 1, length / 3)
        pen.right(120)
        Koch(pen, generation - 1, length / 3)
        pen.left(60)
        Koch(pen, generation - 1, length / 3)



if __name__ == "__main__":
    pen = turtle.Turtle()
    pen.speed(10)
    Snowflake(pen, 4, 500)
    turtle.mainloop()




