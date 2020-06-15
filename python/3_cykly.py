""" 
Prvky, které nám umožní opakované použití stejných příkazů nebo sekvencí příkazů, nazýváme cyklus.

Dělení: řízené podmínkou nebo proměnnou 
- while, while-do - podmínkou
- for - proměnou

Charakteristika cyklu While, Repeat, For, různá interpretace cyklů v různých prostředích 
- např C:
int i = 0;
do {
    printf("%d\n",i);
    i++;
} while (i < 3);
podmínka se rozhodne na konci

int i = 0;
while (i < 3)
{
	printf("%d\n", i);
	i++;
}
podmínka se rozhodne na začátku
stejný výstup, kdyby nebyla podmínka platná od začátku, program nahoře se provede, kdežto program dole se přeskočí

- Cyklus se může breaknout předčasně nebo přeskočit iteraci použitím continue

- V pythonu for loop rozebírá iterbles (list, tuple, range, array, dict, string, ...)
- Zároveň podporuje unpacking, spíš se jedná o foreach:
for i, j, k ... in (range, enumerate, list, tuple... i kombinace):
    #do stuff
    pass

- Zkrácený zápis:
doubled = x*2 for x in list

- Prostředí můžou mít stanovený limit na počet vnoření cyklů, dnes už s tím asi není problém
"""

for i in range(2):
    for j in range(2):
        for k in range(2):
            print("for", i, j, k)


i = 0
while i < 3:
    i += 1
    print("while", i)
else:
    print("while else", i)


def rekurze(i):
    print("rekurze", i)
    if i > 0:
        rekurze(i - 1)
rekurze(3)