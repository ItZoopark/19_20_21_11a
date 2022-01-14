threshold = 67
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

# a = [ [0] * 5 for i in range(5)]
# print(a[1][2])
