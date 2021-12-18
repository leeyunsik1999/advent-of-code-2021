def getNum(file):
    line = file.readline()
    if line:
        return int(line.strip("\n"))
    return False

if __name__ == "__main__":
    text = open("../input.txt", "r")
    line = text.readline()
    prevnum = None
    count = 0
    while line:
        line = line.strip("\n")
        if prevnum == None:
            prevnum = int(line)
        else:
            num = int(line)
            count += 1 if prevnum < num else 0
            prevnum = num
        line = text.readline()
    print(f"Total increases: %d" % (count))
    text.close()