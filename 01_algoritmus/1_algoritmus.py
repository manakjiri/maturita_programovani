"""
Definice: je přesný a srozumitelný návod, jak po konečném počtu kroků dospět od měnitelných vstupních údajů k požadovanému výsledku

Vlastnosti: hromadnost, konečnost, determinovanost, rezultativnost; dále by měl být elementární a srozumitelný

Metody návrhu 
- shoda dolů (Quicksort), 
- zdola nahoru (Backtracking)
- kombinace obou

Způsoby zápisu 
- přirozený jazyk
- odborný jazyk
- grafický zápis
- programovací jazyk (strojový kód, asembler, imperativní jazyky – Pascal, C/C++, SQL, logické a funkcionální jazyky – Prolog, Lisp)

Syntaxe (formální pravidla pro vznik zápisu - jak se to má formálně zapsat)
Sémantika (dává přípustným strukturám význam - co to má dělat)

Fáze řešení algoritmického problému 
- Formulace úlohy - 10%
- Stanovení algoritmu řešení - 30%
- Analýza a optimalizace algoritmu (efektivita v době běhu) - 20%
- Sestavení programu - formalizace - 20%
- Ladění a testování - odstraňování formální chyb a odstraňování skutečných chyb programu - 20%

Příklady – Erathostenovo síto, Euklidův algoritmus, třídicí algoritmy, další
"""

def Erathostenovo(n):
    n += 1
    num_line = list(range(1, n))

    i = 1
    while i <= n**0.5:
        i += 1
        for j in range(2 * i, n, i):
            if j in num_line:
                num_line.remove(j)
    return num_line

def Eukliduv(u, w):
    while w != 0:
        r = u % w
        u = w
        w = r
    return u

print(Eukliduv(300, 100))