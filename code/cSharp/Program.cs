using System;
using System.Collections.Generic;

namespace StonksClicker
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            List<string> STONKS = new List<string>();


            STONKS.Add("INTC");
            STONKS.Add("IBM");
            STONKS.Add("LTC");
            STONKS.Add("WBA");
            STONKS.Add("KMB");
            STONKS.Add("MSFT");
            STONKS.Add("APPL");
            STONKS.Add("T");
            STONKS.Add("TSLA");
            STONKS.Add("KO");
            STONKS.Add("PEP");
            STONKS.Add("ENB");
            STONKS.Add("MAIN");
            STONKS.Add("PBA");
            STONKS.Add("STAG");
            STONKS.Add("SLG");
            STONKS.Add("SJR");
            STONKS.Add("O");
            STONKS.Add("COST");
            STONKS.Add("ADC");

            STONKS.Sort();

            foreach (var item in STONKS)
            {
                Console.WriteLine(item);
            }

            /*
                ADC
                APPL
                COST
                ENB
                IBM
                INTC
                KMB
                KO
                LTC
                MAIN
                MSFT
                O
                PBA
                PEP
                SJR
                SLG
                STAG
                T
                TSLA
                WBA
            */

        }
    }
}
