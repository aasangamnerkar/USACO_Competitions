"""
ID: aasang1
LANG: PYTHON3
PROG: farm
"""

cows = []
N = input()
N = int(N)

for i in range(N):
    temp = input()
    cows.append(temp.split(" "))

cows = [[cow[0], int(cow[1]), int(cow[2])] for cow in cows]

max = 0
for i, item in enumerate(cows):
    if item[1] > max:
        max = item[1]
    if item[2] > max:
        max = item[2]

eaten = [(cow[1], cow[2]) for cow in cows]
steps = [0 for i in range(len(cows))]
moving = [True for i in range(len(cows))]

for x in range(max):
    temp_arr = []

    for i, cow in enumerate(cows):
        if moving[i]:
            if cow[0] == "E":
                next_x = cow[1] + 1
                next_y = cow[2]
            else:
                next_x = cow[1]
                next_y = cow[2] + 1

            if (next_x, next_y) not in eaten:
                cow[1] = next_x
                cow[2] = next_y
                steps[i] += 1
                temp_arr.append((next_x, next_y))
            else:
                moving[i] = False
    eaten += temp_arr

for i, step in enumerate(steps):
    if not moving[i]:
        print(step+1)
    else:
        print("Infinity")
