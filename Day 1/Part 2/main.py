if __name__ == "__main__":
    text = open("../input.txt", "r")
    windows = [0, 0, 0]
    index = 0

    line = text.readline()
    windows[0] += int(line.strip("\n"))

    line = text.readline()
    lineint = int(line.strip("\n"))
    windows[0] += lineint
    windows[1] += lineint

    line = text.readline()
    prevnum = None
    count = 0
    while line:
        lineint = int(line.strip("\n"))
        windows[0] += lineint
        windows[1] += lineint
        windows[2] += lineint
        if prevnum == None:
            prevnum = windows[index]
        else:
            num = windows[index]
            count += 1 if prevnum < num else 0
            prevnum = num
        windows[index] = 0
        index = (index + 1) % 3
        line = text.readline()
    print(f"Total increases: %d" % (count))
    text.close()