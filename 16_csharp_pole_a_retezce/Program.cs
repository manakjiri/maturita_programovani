using System;
// Knihovna s pomocnými funkcemi (Součet prvků)
using System.Linq;
// Knihovna pro práci se seznamem (List)
using System.Collections.Generic;

namespace _16_csharp_pole_a_retezce
{
    class Program
    {
        static void Main(string[] args)
        {
            // Deklarace a inicializace pole
            int[] intArr =  new int[] {5, 6, 9, 10};

            // Práce s polem
            Console.WriteLine("Pole");
            Console.WriteLine($"Výčet prvků: {string.Join(", ", intArr)}");
            Console.WriteLine($"Součet prvků: {intArr.Sum()}");
            Console.WriteLine($"Počet prvků: {intArr.Length}");
            Console.WriteLine($"Aritmetický průměr: {(double)intArr.Sum()/intArr.Length}");
            Console.WriteLine();

            // Deklarace a inicializace seznamu
            List<int> intList = new List<int>();

            // Zápis dat do seznamu pomocí již existujícího pole
            intList.AddRange(intArr);

            // Práce s listem před přidáním nového prvku
            Console.WriteLine("Seznam");
            Console.WriteLine($"Výčet prvků: {string.Join(", ", intList)}");
            Console.WriteLine($"Součet prvků: {intList.Sum()}");
            Console.WriteLine($"Počet prvků: {intList.Count}");
            Console.WriteLine($"Aritmetický průměr: {(double)intList.Sum()/intList.Count}");
            Console.WriteLine();

            // Přidání nového prvku
            intList.Add(20);

            // Práce s listem po přidání prvku
            Console.WriteLine($"Výčet prvků: {string.Join(", ", intList)}");
            Console.WriteLine($"Součet prvků: {intList.Sum()}");
            Console.WriteLine($"Počet prvků: {intList.Count}");
            Console.WriteLine($"Aritmetický průměr: {(double)intList.Sum()/intList.Count}");

            // Konec programu
            Console.ReadLine();
        }
    }
}
