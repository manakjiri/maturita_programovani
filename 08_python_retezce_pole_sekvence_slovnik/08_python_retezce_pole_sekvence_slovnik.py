""" 
Podívejme se, jak Python pracuje se složitějšími datovými typy. Řekneme si něco o řetězcích, seznamech a uspořádaných n-ticích, ukážeme si indexování a slicing, a nakonec si ukážeme, jak se vytvoří slovník a jak se sním pracuje 

Řetězec – string (neměnitelný), „“ nebo ‚‘ 
Ukázka Seznam – list (měnitelný) s = [s1, s2, „tři“, [4, „čtyři“]] 
Uspořádané n-tice (neměnitelná) n = (1, „A“, 3) 
Rozsah – range (neměnitelná) range(konec), range(začátek,konec,krok) 
Slicing – t[1:4], t[:2], t[2:] Funkce – x in s, del s[i], len(s), s.index(x), s.append(x), s.remove(x), s.count(x) 
Slovník – s {„klic1“ : hodnota1, „klic2“: hodnota2} přidání / změna položky – s[„klic“] = hodnota, smazání položky sezamu – del s[„klic“]  – podmínky, cykly
"""

# Zároveň příklady ITERABLES
# string
s = 'Podívejme se, jak Python pracuje se složitějšími datovými typy.'
# list
l = [1, 2, 'tři', [4, 'čtyři']]
# tuple
t = (1, 'A', 3) 
# range
r = range(0, 8, 2)
# dictionary
d = {
    'jako': 'klic', 
    'a': {
        'item': 'muze', 
        'byt': 'cokoliv'
    }
}


d['novy'] = ['klic', 'a', 'item']
d['a']['slovniky'] = 'jsou uzasne'
del(d['jako'])
print(d['a'].values())

print('slicing:', [s[0:10], s[-10:-1], s[::3], r[0:2]])

print('count of "a":', s.count('a'))

print('iterables:')
s = s.split()
for i in [s, l, t, r, d]:
    for j in i:
        print(j)

print('zip magic:')
for i in zip(s, l, r):
    print(i)


