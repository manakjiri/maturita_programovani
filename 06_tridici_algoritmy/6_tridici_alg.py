""" 
Slouží k seřazení prvků vstupního seznamu dle požadovaného klíče, na takové seřazení jsou kladeny určité požadavky, z nich nejčastější je rychlost řazení 

Nejoptimálnější nejsou algoritmy, které porovnávají prvky, ale nejsou vhodné k obecnému využití 
Nejoptimálnější porovnávací algoritmy mají složitost n x log(n), u menších souborů n x n 

Vlastnosti: stabilita, přirozenost
"""
from random import randint

def BubbleSort(numList):
    sorted = False
    lastIndex = len(numList) - 1
    while not(sorted):
        sorted = True
        for i in range(lastIndex):
            if numList[i] > numList[i + 1]:
                numList[i], numList[i + 1] = numList[i + 1], numList[i]
                sorted = False
        # print(numList)
        lastIndex -= 1

if __name__ == "__main__":
    numbers = []
    for i in range(10):
        numbers += [randint(0, 100)]
    print("Zadani:")
    print(numbers)
    print()
    BubbleSort(numbers)
    print("Vysledek:")
    print(numbers)