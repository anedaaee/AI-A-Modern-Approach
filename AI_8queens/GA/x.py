def getValue(state):
    value = 0
    for y1 in range(0, len(state)):
        for y2 in range(y1 + 1, len(state)):
            x1 = state[y1]
            x2 = state[y2]
            if (x1 == x2):
                value += 1
            elif (y1 == y2):
                value += 1
            else:
                dx = abs(x2 - x1)
                dy = abs(y2 - y1)
                if (dx == dy):
                    value += 1

    return value

print(str(getValue([0,1,2,3,4,5,6,7])))