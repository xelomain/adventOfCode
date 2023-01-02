using System.Text.RegularExpressions;

namespace Day11 {
    internal class Monkey {
        public int Name { get; set; }
        public List<double> Items { get; set; }
        public string Operation { get; set; }
        public double Divided { get; set; }
        public int TestFailed { get; set; }
        public int TestSuccess { get; set; }
        public double Inspected { get; set; }
    }

    internal class Program {

        static List<Monkey> GetStartValues ( string[] input ) {
            List<Monkey> result = new List<Monkey>();
            Monkey currentMonkey = null!;
            string regexForNumbers = @"(\d+)";
            foreach (string line in input) {
                if (line.Trim().Equals("")) {
                    result.Add(currentMonkey!);
                    currentMonkey = null!;
                    continue;
                }
                if (line.Trim().StartsWith("Monkey")) {
                    currentMonkey = new Monkey();
                    Match match = Regex.Match(line, regexForNumbers);
                    currentMonkey.Name = Int32.Parse(match.Groups[1].Value);
                    currentMonkey.Items = new List<double>();
                    currentMonkey.Inspected = 0;
                    continue;
                }
                if (line.Trim().StartsWith("Starting items")) {
                    foreach (var t in line.Trim().Split(':')[1].Split(',')) {
                        currentMonkey!.Items.Add(int.Parse(t));
                    }
                    continue;
                }
                if (line.Trim().StartsWith("Operation")) {
                    currentMonkey!.Operation = line.Trim();
                    continue;
                }
                if (line.Trim().StartsWith("Test")) {
                    Match match = Regex.Match(line.Trim(), regexForNumbers);
                    currentMonkey!.Divided = Int32.Parse(match.Groups[1].Value);
                    continue;
                }
                if (line.Trim().StartsWith("If true")) {
                    Match match = Regex.Match(line.Trim(), regexForNumbers);
                    currentMonkey!.TestSuccess = Int32.Parse(match.Groups[1].Value);
                    continue;
                } else {
                    Match match = Regex.Match(line.Trim(), regexForNumbers);
                    currentMonkey!.TestFailed = Int32.Parse(match.Groups[1].Value);
                    continue;
                }
            }

            result.Add(currentMonkey!);

            return result;
        }

        public static double newValue ( string operation, double v ) {
            string regex = @"old (\*|\+) (\d+|old)";
            Match match = Regex.Match(operation, regex);
            if (match.Success) {
                double secound = 0;
                if (match.Groups[2].Value == "old") {
                    secound = v;
                } else {
                    secound = int.Parse(match.Groups[2].Value);
                }

                if (match.Groups[1].Value == "+") {
                    return secound + v;
                } else {
                    return secound * v;
                }
            }
            return 0;
        }

        public static void part1 ( string[] input ) {
            List<Monkey> start = GetStartValues(input);
            for (int round = 0; round < 20; round++) {
                foreach (Monkey monkey in start) {
                    for (int i = 0; i < monkey.Items.Count; i++) {
                        monkey.Inspected++;
                        double value = newValue(monkey.Operation, monkey.Items.ElementAt(i));
                        //math.Floor gibt die größte Ganzzahl zurück, die kleiner oder gleich der angegebenen Zahl ist
                        var newWorryLevel = Math.Floor(value / 3.0);
                        if (newWorryLevel % monkey.Divided == 0) {
                            start.Where(x => x.Name == monkey.TestSuccess).First().Items.Add((int)newWorryLevel);
                        } else {
                            start.Where(x => x.Name == monkey.TestFailed).First().Items.Add((int)newWorryLevel);
                        }
                    }
                    monkey.Items.Clear();
                }
            }
            Console.WriteLine(start.Select(x => x.Inspected).OrderByDescending(x => x).Take(2).Aggregate(( a, x ) => a * x));
        }

        static void Main ( string[] args ) {

            var inputFile = File.ReadAllLines(@"C:\Temp\adventofcode\adventOfCode\Day11\Day11\Day11\puzzleInput11.txt");
            List<string> input = new List<string>(inputFile);

            part1(input.ToArray());
        }
    }
}