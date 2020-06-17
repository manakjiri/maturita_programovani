using System;
using System.Collections.Generic;

namespace _17_csharp_osetreni_vyjimek
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Začátek programu");
            MemoryException();
            Console.WriteLine("Konec programu");
        }

        public static void MemoryException()
        {
            int a = 0;
            List<int> list = new List<int>();
            while (a != -1)
            {
                list.Add(a++);
            }
            /*try
            {
                while (a != -1)
                {
                    list.Add(a++);
                }
            }
            catch (System.OutOfMemoryException)
            {
                Console.WriteLine("Kupte více pamětí.");
            }
            finally
            {
                Console.WriteLine("Výjimka zachycena.");
            }*/
        }
    }
}
