using System;
using System.Collections.Generic;

namespace Meme
{
    class Program
    {
        public static void Main(string[] args)
        {
            List<string> t = new List<string>{"abc", "def", "ghi"};
            for (int y = 0; y < t.Count; y++)
            {
                for (int x = 0; x < t[y].Length; x++)
                {
                    if (t[y][x].ToString() == "a")
                    {
                        Console.WriteLine(t[y][x]);
                    }
                }
            }
        }
    }
}
