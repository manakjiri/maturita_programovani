s = """ 
Knihovna pro práci s grafikou a její zavedení – import tkinter
Okno a jeho nastavení – okno = tkinter.Tk()
Pracovní plocha – canvas = tkniter.Canvas()
Základní příkazy – create_line, create_rectangle, create_oval, create_text
"""

import tkinter as tk
from random import randint

def art():
    rnd = lambda: randint(0, 400)
    canvas.create_rectangle(rnd(), rnd(), rnd(), rnd())
    canvas.create_oval(rnd(), rnd(), rnd(), rnd())
    canvas.create_line(rnd(), rnd(), rnd(), rnd(), fill="green")
    canvas.create_line(rnd(), rnd(), rnd(), rnd(), fill="red", dash=(4, 4))
    canvas.create_text(rnd(), rnd(), text= s.split()[randint(0, len(s.split())-1)], fill='yellow')


okno = tk.Tk()
okno.geometry('500x400')

canvas = tk.Canvas(okno, width=400, height=400)
canvas.pack(side='left')

art()
btn = tk.Button(okno, text='art', width=4, height=2, command=art)
btn.pack(side='right')

okno.mainloop()
