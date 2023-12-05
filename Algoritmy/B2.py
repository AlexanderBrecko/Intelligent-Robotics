import time
import numpy


def solver(cesta):
    f = open("B1.txt", "r")

    bludisko = []

    for i in range(10):
        bludisko.append(f.readline())
        bludisko[i] = bludisko[i].replace('\n', '')
        bludisko[i] = bludisko[i].replace('S', '#')

    x, y, m, n = 0, 0, 0, 0
    for i in range(10):
        for j in range(10):
            if bludisko[i][j] == "#":
                x = i
                y = j
            if bludisko[i][j] == "K":
                m = i
                n = j

    for k in range(20):
        if cesta[k + 1] == "U":
            try:
                if bludisko[x - 1][y] == " ":
                    bludisko[x - 1] = bludisko[x - 1][:y] + "#" + bludisko[x - 1][y + 1:]
                    x = x - 1
                    y = y
            except IndexError:
                pass
        if cesta[k + 1] == "D":
            try:
                if bludisko[x + 1][y] == " ":
                    bludisko[x + 1] = bludisko[x + 1][:y] + "#" + bludisko[x + 1][y + 1:]
                    x = x - 1
                    y = y
            except IndexError:
                pass
        if cesta[k + 1] == "L":
            try:
                if bludisko[x][y - 1] == " ":
                    bludisko[x] = bludisko[x][:y - 1] + "#" + bludisko[x][y:]
                    x = x
                    y = y - 1
            except IndexError:
                pass
        if cesta[k + 1] == "R":
            try:
                if bludisko[x][y + 1] == " ":
                    bludisko[x] = bludisko[x][:y + 1] + "#" + bludisko[x][y + 2:]
                    x = x
                    y = y + 1
            except IndexError:
                pass

        # for l in range(7): print()
        # print("\n".join(bludisko))
        # for l in range(8): print()
        # time.sleep(0.4)

    return (numpy.abs(m - x) + numpy.abs(n - y))  # hodnota od ciela


rodic = ["0LLLLLLLLLLLLLLLLLLLL",
         "0RRRRRRRRRRRRRRRRRRRR",
         "0UUUUUUUUUUUUUUUUUUUU",
         "0DDDDDDDDDDDDDDDDDDDD"]

dieta = ["0LLLLLLLLLLLLLLLLLLLL",
         "0RRRRRRRRRRRRRRRRRRRR",
         "0UUUUUUUUUUUUUUUUUUUU",
         "0DDDDDDDDDDDDDDDDDDDD"]

for generacia in range(1000):

    for i in range(4):
        a = solver(rodic[i])
        rodic[i] = chr(48 + a) + rodic[i][1:]

    rodic.sort(reverse=False)

    print(rodic)

    dieta[0] = rodic[0]
    for i in range(3):
        for gen in range(10):
            a = numpy.random.randint(1, 21)
            dieta[i + 1] = rodic[0][0:a] + rodic[i + 1][a] + rodic[0][a + 1:]

    if (generacia % 5 == 0):
        a = numpy.random.randint(1, 21)
        b = numpy.random.randint(1, 4)
        c = numpy.random.randint(4)
        if c == 0: d = "U"
        if c == 1: d = "D"
        if c == 2: d = "L"
        if c == 3: d = "R"
        dieta[b] = dieta[b][:a] + d + dieta[b][a + 1:]

    rodic = dieta

