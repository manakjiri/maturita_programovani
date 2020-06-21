import turtle

clr = 0
inc = 0.005

colors = ['red', 'orange', 'gold', 'navajo white', 'spring green', 'lime', 'cyan', 'green', 'blue', 'indigo', 'purple', 'navy', 'brown']

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


def Gosper(pen, generation, length):
    pen.pu()
    pen.pensize(3)
    pen.setpos(0, -150)
    pen.pd()
    Gosper_L(pen, generation, length)

def Gosper_L(pen, generation, length):
    global clr
    clr += inc
    if generation > 0:
        Gosper_L(pen, generation - 1, length)
        pen.left(60)
        Gosper_R(pen, generation - 1, length)
        pen.left(120)
        Gosper_R(pen, generation - 1, length)
        pen.right(60)
        Gosper_L(pen, generation - 1, length)
        pen.right(120)
        Gosper_L(pen, generation - 1, length)
        Gosper_L(pen, generation - 1, length)
        pen.right(60)
        Gosper_R(pen, generation - 1, length)
        pen.left(60)
    else:
        pen.pencolor(color_to_hex(clr))
        pen.fd(length)

def Gosper_R(pen, generation, length):
    global clr
    clr += inc
    if generation > 0:
        pen.right(60)
        Gosper_L(pen, generation - 1, length)
        pen.left(60)
        Gosper_R(pen, generation - 1, length)
        Gosper_R(pen, generation - 1, length)
        pen.left(120)
        Gosper_R(pen, generation - 1, length)
        pen.left(60)
        Gosper_L(pen, generation - 1, length)
        pen.right(120)
        Gosper_L(pen, generation - 1, length)
        pen.right(60)
        Gosper_R(pen, generation - 1, length)
    else:
        pen.pencolor(color_to_hex(clr))
        pen.fd(length)

def color_to_hex(c):
    #return f'#{hex(int(RGB_tuples[clr][0] * 255))}{hex(int(RGB_tuples[clr][1] * 255))}{hex(int(RGB_tuples[clr][2] * 255))}'.replace('0x', '')
    global clr
    if clr >= len(colors):
        clr = 0
    return colors[int(clr)]

if __name__ == "__main__":
    pen = turtle.Turtle()
    pen.speed(0)
    #Snowflake(pen, 4, 500)
    Gosper(pen, 4, 10)
    turtle.mainloop()




