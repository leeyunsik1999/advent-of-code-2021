if __name__ == "__main__":
    file = open("../input.txt", "r")
    distance = 0
    depth = 0
    aim = 0
    line = file.readline()
    while line:
        params = line.strip('\n').split(" ")
        params[1] = int(params[1])

        if params[0] == 'up':
            aim -= params[1]
        elif params[0] == 'down':
            aim += params[1]
        else:
            distance += params[1]
            depth += aim * params[1]

        line = file.readline()
    print(f"Distance: %d, Depth: %d, Multiplied: %d" % (distance, depth, distance*depth))
    file.close()