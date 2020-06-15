"""
Jeden ze základních stavebních prvků je podmínka (podmíněný blok, rozhodovací blok, alternativa) 

V různých jazycích implementován různě – asembler má logický výraz se skokem na adresu pomocí instrukce jump, basic má řešeno pomocí příkazu goto, Pascal jednoduchý if – then – else, podobně i jazyk C 

Podmínky (logické výrazy) formulovány na základě Boolovské logiky 
- Neúplná podmínka, úplná podmínka, vnořená podmínka, vícenásobná podmínka 
"""

a = 3
b = 50
c = 10

if a > b and a > c:
    print("a")
elif b > a and b > c:
    print("b")
else:
    print("c")

if a > b:
    if a > c:
        print("a")
    else:
        print("c")
else:
    if b > c:
        print("b")
    else:
        print("c")

if b > c:
    pass
else: 
    b = c
if a > b:
    pass
else:
    a = b
print(a)
