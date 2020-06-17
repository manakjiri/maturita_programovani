using System;

namespace Classes
{
    class Program
    {
        static void Main(string[] args)
        {
            Dog dog = new Dog();
            dog.NumberOfLegs();
            dog.MakeSound();
            Bird bird = new Bird();
            bird.NumberOfLegs();
            bird.MakeSound();
            // Console.ReadLine();
        }

        public class Animal
        {
            protected int numberOfLegs;
            protected string sound;

            public void NumberOfLegs()
            {
                Console.WriteLine("I have {0} legs.", numberOfLegs);
            }

            public void MakeSound()
            {
                Console.WriteLine(sound);
            }

            protected Animal()
            {
                Console.WriteLine("{0} has been created.", this.GetType().Name);
            }
        }
        public class Dog : Animal
        {
            public Dog()
            {
                numberOfLegs = 4;
                sound = "Woof! Woof!";
            }
        }

        public class Bird : Animal
        {
            public Bird()
            {
                numberOfLegs = 2;
                sound = "Peep, peep.";
            }
        }
    }
}