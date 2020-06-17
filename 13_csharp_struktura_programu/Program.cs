using System;

namespace Structure
{
    namespace Functions
    {
        class Prime
        {
            public static bool IsPrime(int number)
            {
                if (number < 2)
                {
                    return false;
                }
                else
                {
                    for (int i = 2; i <= Math.Sqrt(number); i++)
                    {
                        if (number % i == 0)
                        {
                            return false;
                        }
                    }
                }
                return true;
            }
        }
    }
    class Program
    {
        public static void Main()
        {
            int[] tested = new int[5] { 5, 2, 1, 1223, -29};
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("{0} {1} prvočíslo.", tested[i], Functions.Prime.IsPrime(tested[i]) ? "je" : "není");
            }
        }
    }
}