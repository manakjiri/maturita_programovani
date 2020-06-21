using System;
using System.Collections.Generic;

namespace _17_csharp_osetreni_vyjimek
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> intList = new List<int>();
            try
            {
                int b = 0;
                // while(b == 0) intList.Add(5);
                int a = 5 / b;
            }
            catch (DivideByZeroException)
            {
                Console.WriteLine("Detekováno dělení nulou.");
            }
            catch (OutOfMemoryException)
            {
                Console.WriteLine("Využita veškerá paměť.");
            }
            finally
            {
                Console.WriteLine("Program funguje nadále.");
            }
            Console.ReadLine();
        }
    }
}
