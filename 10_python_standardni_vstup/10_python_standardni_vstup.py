""" 
Standardním vstupem z pohledu programování chápeme vstup z klávesnice, i když z uživatelského hlediska jsou to další periferní zařízení jako myš, skener atd. 

Podívejme se blíže na vstup z klávesnice. Ten můžeme realizovat pomocí funkce input nebo pomocí funkce getch(), která je součástí knihovny msvcrt. 

V dalším budeme předpokládat, že uživatel zadává hodnoty a potvrzuje je klávesou Enter, proto se zaměříme na funkci input, která nám jako vstupní funkce plně postačuje. Je třeba zmínit, že různé verze jazyka Python se ke vstupním hodnotám chovají různě, například verze 2 brala vstup jako výraz, verze 3 bere vstup jako řetězec a jeho zpracování ponechává plně na programátorovi, to bylo ve starších verzích možné pouze pomocí funkce raw_input. 

Ukázka – input(), přetypování int(input()) Pro načítání více hodnot oddělených mezerou nebo jiným oddělovačem se dá použít funkce split(), syntaxe input().split(), ukažte příklad. Tím však získáme pole řetězců, což nám pro pár hodnot nebude vadit, výstup můžeme přetypovat int(pole[1]). U více hodnot můžeme použít cyklus, který nám tento problém odstraní, nebo využijeme funkci map, která provede požadované přetypování pro všechny prvky seznamu. 

Ukažte příklad pole = map(int, input().split()). To nám ale vrátí objekt, my bychom chtěli získat seznam, proto ještě celou funkci obalíme přetypováním na seznam. Příklad pole = list(map(int, input().split())). 
"""

pole = list(map(int, input().split()))
print(pole)

# jednoduchy arg parse pro zadavani parametru pri spusteni programu z konzole
args = input('args: ').split()
settings = {}
last = ''
for a in args:
    if '-' in a:
        last = a
        settings[last] = []
    elif last:
        settings[last].append(a)

print(settings)

# asi taky umime
