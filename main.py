def one(threshold):
    # threshold = 67
    a = [0] * threshold

    for s in range(len(a)):
        if s * 5 >= threshold:
            a[s] = 1

    start_pos = (threshold - 1) // 5

    for s in range(start_pos, 0, -1):
        if a[s + 1] > 0 and a[s + 4] > 0 and a[s * 5] > 0:
            a[s] = - max(a[s + 1], a[s + 4], a[s * 5])
        elif a[s + 1] < 0 or a[s + 4] < 0 or a[s * 5] < 0:
            res = filter(lambda x: x < 0, [a[s + 1], a[s + 4], a[s * 5]])
            a[s] = abs(max(res)) + 1
    print(a)
    print()
    for s in range(len(a)):
        if a[s] == -2:
            print(s)


def two():
    a = [[0] * 70 for i in range(70)]
    for s_row in range(69):
        for s_col in range(69):
            if s_row * 2 + s_col >= 77 or s_row + s_col * 2 >= 77:
                a[s_row][s_col] = 1

    for k in range(50):
        for s_row in range(35):
            for s_col in range(35):
                if a[s_row][s_col] == 0:
                    if a[s_row + 1][s_col] > 0 and a[s_row * 2][s_col] > 0 and a[s_row][s_col + 1] > 0 and a[s_row][
                        s_col * 2] > 0:
                        a[s_row][s_col] = - max(a[s_row + 1][s_col], a[s_row * 2][s_col], a[s_row][s_col + 1],
                                                a[s_row][s_col * 2])
                    elif a[s_row + 1][s_col] < 0 or a[s_row * 2][s_col] < 0 or a[s_row][s_col + 1] < 0 or a[s_row][
                        s_col * 2] < 0:
                        res = filter(lambda x: x < 0, [a[s_row + 1][s_col], a[s_row * 2][s_col], a[s_row][s_col + 1],
                                                       a[s_row][s_col * 2]])
                        a[s_row][s_col] = abs(max(res)) + 1
    for s in range(70):
        if a[7][s] == -2:
            print(s)


def two_27765():
    max_stones = 59
    start_win = 69
    a = [[0] * max_stones for i in range(max_stones)]
    for i in range(max_stones):
        for j in range(max_stones):
            if i * 2 + j >= start_win or i + j * 3 >= start_win:
                a[i][j] = 1

    for k in range(500):
        for i in range(30):
            for j in range(20):
                if a[i][j] == 0:
                    if a[i + 1][j] > 0 and a[i][j + 1] > 0 and a[i * 2][j] > 0 and a[i][j * 3] > 0:
                        a[i][j] = - max(a[i + 1][j], a[i][j + 1], a[i * 2][j], a[i][j * 3])
                    elif a[i + 1][j] < 0 or a[i][j + 1] < 0 or a[i * 2][j] < 0 or a[i][j * 3] < 0:
                        res = filter(lambda x: x < 0, [a[i + 1][j], a[i][j + 1], a[i * 2][j], a[i][j * 3]])
                        a[i][j] = abs(max(res)) + 1
    for s in range(max_stones):
        if a[10][s] == 2:
            print(s)


# two_27765()


# a = [ [0] * 5 for i in range(5)]
# print(a[1][2])
# ДЗ: Запрограммировать задачу с двумя кучами!!!
def one_4111(turns):
    threshold = 64
    a = [0] * (threshold + 1)
    # победа 1-ым ходом
    for s in range(len(a)):
        if threshold <= s * 3 <= 100:
            a[s] = 1

    a[threshold] = 1
    # ходы меньшим ходом после победы одним ходом
    for s in range(threshold - 1, 100 // 3, -1):
        if a[s + 1] > 0:
            a[s] = -a[s + 1]
        else:
            a[s] = abs(a[s + 1]) + 1

    start_pos = (threshold - 1) // 3

    for s in range(start_pos, 0, -1):
        if a[s + 1] > 0 and a[s * 3] > 0:
            a[s] = - max(a[s + 1], a[s * 3])
        elif a[s + 1] < 0 or a[s * 3] < 0:
            res = filter(lambda x: x < 0, [a[s + 1], a[s * 3]])
            a[s] = abs(max(res)) + 1
    print(a)
    for turn in turns:  # turns = [2, -2]
        for s in range(len(a)):  # turn =-2
            if a[s] == turn:
                print(s, end=' ')
        print()


# one_4111([-1, 2, -2])

def one_3074(turns):
    threshold = 999
    a = [0] * (threshold + 1)

    for s in range(len(a)):
        if s * 2 >= threshold:
            a[s] = 1

    start_pos = (threshold - 1) // 2

    for s in range(start_pos, 0, -1):
        if a[s + 100] > 0 and a[s * 2] > 0:
            a[s] = - max(a[s + 100], a[s * 2])
        elif a[s + 100] < 0 or a[s * 2] < 0:
            res = filter(lambda x: x < 0, [a[s + 100], a[s * 2]])
            a[s] = abs(max(res)) + 1
    print(a)
    res = []
    for i in range(len(turns)):
        count = 0
        for s in range(len(a)):
            if a[s] == turns[i]:
                if i == len(turns) - 1:
                    res.append(s)
                else:
                    count += 1
        if i == len(turns) - 1:
            print(max(res), min(res))
        else:
            print(count)


one()
one_3074([-1, 2, -2])
