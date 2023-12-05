import time

f = open("B1.txt", "r")

bludisko = []

for i in range(10):
    bludisko.append(f.readline())
    bludisko[i] = bludisko[i].replace('\n', '')
    bludisko[i] = bludisko[i].replace('K', '0')
    bludisko[i] = bludisko[i].replace('S', '#')

print("\n".join(bludisko))
path = 0

for k in range(30):
    for i in range(10):
        for j in range(10):
            if bludisko[i][j] == chr(48 + k):
                try:
                    if bludisko[i - 1][j] == "#":
                        path = k
                    if bludisko[i - 1][j] == " ":
                        bludisko[i - 1] = bludisko[i - 1][:j] + chr(49 + k) + bludisko[i - 1][j + 1:]
                except IndexError:
                    print()
                try:
                    if bludisko[i + 1][j] == "#":
                        path = k
                    if bludisko[i + 1][j] == " ":
                        bludisko[i + 1] = bludisko[i + 1][:j] + chr(49 + k) + bludisko[i + 1][j + 1:]
                except IndexError:
                    print()
                try:
                    if bludisko[i][j - 1] == "#":
                        path = k
                    if bludisko[i][j - 1] == " ":
                        bludisko[i] = bludisko[i][:j - 1] + chr(49 + k) + bludisko[i][j:]
                except IndexError:
                    print()
                try:
                    if bludisko[i][j + 1] == "#":
                        path = k
                    if bludisko[i][j + 1] == " ":
                        bludisko[i] = bludisko[i][:j + 1] + chr(49 + k) + bludisko[i][j + 2:]
                except IndexError:
                    print()

    for l in range(7): print()
    print("\n".join(bludisko))
    for l in range(8): print()
    time.sleep(0.8)

print(path)
x = 0
y = 0

for i in range(10):
    for j in range(10):
        if bludisko[i][j] == "#":
            x = i
            y = j

for k in range(path + 1):
    try:
        if bludisko[x - 1][y] == chr(48 + path - k):
            bludisko[x - 1] = bludisko[x - 1][:y] + "#" + bludisko[x - 1][y + 1:]
            x = x - 1
            y = y
    except IndexError:
        print()
    try:
        if bludisko[x + 1][y] == chr(48 + path - k):
            bludisko[x + 1] = bludisko[x + 1][:y] + "#" + bludisko[x + 1][y + 1:]
            x = x + 1
            y = y
    except IndexError:
        print()
    try:
        if bludisko[x][y - 1] == chr(48 + path - k):
            bludisko[x] = bludisko[x][:y - 1] + "#" + bludisko[x][y:]
            x = x
            y = y - 1
    except IndexError:
        print()
    try:
        if bludisko[x][y + 1] == chr(48 + path - k):
            bludisko[x] = bludisko[x][:y + 1] + "#" + bludisko[x][y + 2:]
            x = x
            y = y + 1
    except IndexError:
        print()

    for l in range(7): print()
    print("\n".join(bludisko))
    for l in range(8): print()
    time.sleep(0.8)