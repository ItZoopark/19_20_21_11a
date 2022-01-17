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


two()

# a = [ [0] * 5 for i in range(5)]
# print(a[1][2])
# ДЗ: Запрограммировать задачу с двумя кучами!!!
