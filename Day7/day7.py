def readInput():
    input = open("puzzleInput7.txt", "r")
    readFile = input.read()
    newInput = readFile.split('\n')
    return newInput

def daySeven():

    input = readInput()

    dirs = {"/home":0}
    path = "/home"

    for command in input:
        if command[0] == "$":
            if command[2:4] == "ls":
                pass
            elif command[2:4] == "cd":
                if command[5:6] == "/":
                    path = "/home"
                elif command[5:7] == "..":
                    path = path[0:path.rfind("/")]
                else:
                    dirName = command[5:]              
                    path = path + "/" + dirName        
                    dirs.update({path:0})              
        elif command[0:3] == "dir":
            pass
        else:
            size = int(command[:command.find(" ")])     
            dir = path
            for i in range(path.count("/")):
                dirs[dir] += size
                dir = dir[:dir.rfind("/")]

    total = 0
    limit = 30000000 - (70000000 - dirs["/home"])
    validDirs = []

    for dir in dirs:

        #Teil 1
        #if dirs[dir] < 100000:
        #    total += dirs[dir]

        #Teil2
        if limit <= dirs[dir]:
            validDirs.append(dirs[dir])
            total = min(validDirs)
    
    return total

ergebnis = daySeven()
print(ergebnis)