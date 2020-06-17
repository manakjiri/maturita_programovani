using System;
// Knihovna s pomocnými funkcemi (Součet a počet prvků)
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
            Console.WriteLine($"Vstup: {string.Join(", ", intArr), 10}");
            Console.WriteLine($"Součet prvků: {intArr.Sum()}");
            Console.WriteLine($"Počet prvků: {intArr.Count()}");

            // Deklarace a inicializace seznamu
            List<int> intList = new List<int>();
            List<object> objectList = new List<object>();

            object[] objArr = new object[] {intArr, 5, "asd", 59};
            Console.WriteLine($"Vstup: {string.Join(", ", objArr), 10}");
            Console.WriteLine(((string)objArr[2])[2]);
            Console.WriteLine($"{objArr[0].GetType().ToString()}, {objArr[1].GetType().ToString()}, {objArr[2].GetType().ToString()}");
            // Zápis dat do seznamu
            intList.AddRange(intArr);

            Console.ReadLine();
        }
    }
}
