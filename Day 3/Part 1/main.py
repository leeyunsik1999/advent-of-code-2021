def get_num(store, inverse=False):
    sum = 0
    for i in range(12):
        binary = (1 if store[i][1] >= store[i][0] else 0) if not inverse else (0 if store[i][1] >= store[i][0] else 1)
        sum += binary * (2**(11 - i))
    return sum


if __name__ == "__main__":
    store = []
    for x in range(12):
        store.append([0, 0])
    
    file = open("../input.txt", "r")
    line = file.readline()
    while line:
        line = line.strip('\n')
        for i in range(len(line)):
            if line[i] == '0':
                store[i][0] += 1
            else:
                store[i][1] += 1
        line = file.readline()
    print(get_num(store))
    print(get_num(store, inverse=True))
    print(get_num(store) * get_num(store, inverse=True))