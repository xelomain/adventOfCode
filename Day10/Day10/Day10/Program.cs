
namespace Day10 {
    internal class Program {

        static int signalStaerke ( int cycles, int registerX) {
            if ((cycles - 20) % 40 == 0) {
                return registerX * cycles;
            }
            return 0;
        }

        static void part1 ( ) {
            int cycles = 0;
            int registerX = 1;
            int signalSumme = 0;

            var inputFile = File.ReadAllLines(@"C:\Temp\adventofcode\adventOfCode\Day10\Day10\Day10\puzzleInput10.txt");
            List<string> input = new List<string>(inputFile);


            foreach (var call in input) {
                if (call == "noop") {
                    cycles++;
                    signalSumme += signalStaerke(cycles, registerX);
                    continue;
                }
                if (call.StartsWith("addx")) {
                    for (int i = 0; i < 2; i++) {
                        cycles++;
                        signalSumme += signalStaerke(cycles, registerX);
                        if (i == 1) {
                            registerX += Convert.ToInt32(call.Split(" ")[1]);
                        }
                    }
                }
            }
            Console.WriteLine(signalSumme);
        }

        static int[] spritePos(int registerX, int cycles ) {
            registerX += (cycles / 40) * 40;
            return new int[] {
                registerX,
                registerX+1,
                registerX+2
            };
        }

        static string[,] cRT ( int cycles, int registerX, string[,] crtMap ) {
            var zeichen = spritePos(registerX, cycles).Contains(cycles) ? "#" : ".";
            crtMap[cycles / 40, cycles % 40] = zeichen;
            return crtMap;
        }


        static void part2 ( ) {
            int cycles = 0;
            int registerX = 0;
            var crtMap = new string[6, 40];

            var inputFile = File.ReadAllLines(@"C:\Temp\adventofcode\adventOfCode\Day10\Day10\Day10\puzzleInput10.txt");
            List<string> input = new List<string>(inputFile);

            foreach (var call in input) {
                if (cycles == (6 * 40) - 1) break;

                if (call == "noop") {
                    crtMap = cRT(cycles, registerX, crtMap);
                    cycles++;
                    continue;
                }
                if (call.StartsWith("addx")) {
                    for (int i = 0; i < 2; i++) {
                        crtMap = cRT(cycles, registerX, crtMap);
                        cycles++;
                        if (i == 1) {
                            registerX += Convert.ToInt32(call.Split(" ")[1]);
                        }
                    }
                }
            }

            for (int row = 0; row < 6; row++) {
                for (int col = 0; col < 40; col++) {
                    string build = crtMap[row, col];
                    Console.Write(build);
                }
                Console.WriteLine();
            }

        }

        static void Main ( string[] args ) {

            //part1();
            part2();

        }
    }
}