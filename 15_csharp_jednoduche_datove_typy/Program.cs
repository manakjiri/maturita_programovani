using System;

namespace _15_csharp_datove_typy
{
    class Program
    {
        static void Main(string[] args)
        {
            // Ukázka rozdílu mezi řetězcem (string) a celým číslem (int) 

            string a, b, c;
            Console.Write("Zadejte první celočíselnou hodnotu: ");
            a = Console.ReadLine();

            Console.Write("Zadejte druhou celočíselnou hodnotu: ");
            b = Console.ReadLine();

            Console.Write("Zadejte třetí celočíselnou hodnotu: ");
            c = Console.ReadLine();

            Console.WriteLine($"Vstupní hodnoty {a}, {b}, {c}");

            Console.WriteLine("Výstup sčítání celých čísel");
            Console.WriteLine(int.Parse(a) + int.Parse(b) + int.Parse(c));

            Console.WriteLine("Výstup Sčítání řetězců");
            Console.WriteLine(a + b + c);

            Console.WriteLine();

            // Porovnání rozsahu číselných hodnot různých datových typů
            Console.WriteLine("Datový typ od Minimální hodnota do Maximální hodnota");
            Console.WriteLine($"Integer od {int.MinValue} do {int.MaxValue}");
            Console.WriteLine($"Float od {float.MinValue} do {float.MaxValue}");
            Console.WriteLine($"Double od {double.MinValue} do {double.MaxValue}");
            Console.WriteLine($"Decimal od {decimal.MinValue} do {decimal.MaxValue}");
            
            // Konec programu
            Console.ReadLine();
        }
    }
}
