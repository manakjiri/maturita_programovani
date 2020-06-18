""" 
Definice: složitost algoritmů udává, jak je daný algoritmus rychlý, pro zjednodušení se zavádí pojem asymptotická složitost, což je rozdělení algoritmů do tříd složitosti, co to znamená, popis dvou algoritmů ze stejné třídy a dvou algoritmů z různých tříd, obrázek 

Složitost se určí jako počet elementárních operací, pro zjednodušení počet porovnání 

Dolní odhad omicron, horní odhad omega, asymptotická shodnost theta

https://ksi.fi.muni.cz/ulohy/274
"""

from time import time

n_casy = []
n2_casy = []

samples = 10
n = 100
n_mult = 2

for run in range(samples):
    print(f'Run {run} (n = {n}):')
    
    cas = time()
    for i in range(n):
        pass
    cas = time() - cas
    n_casy.append(cas)
    print(f'N:   {cas}')

    cas = time()
    for i in range(n):
        for j in range(n):
            pass
    cas = time() - cas
    n2_casy.append(cas)
    print(f'N^2: {cas}')

    n *= n_mult

print(f'Times avg:\nN:   {sum(n_casy) / samples}\nN^2: {sum(n2_casy) / samples}')

