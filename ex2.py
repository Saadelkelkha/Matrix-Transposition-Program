t = []

for i in range(5):
    l = []
    for j in range(5):
        n = int(input("Enter a number: "))
        l.append(n)
    t.append(l)

for i in range(5):
    for j in range(i, 5):
        t[i][j], t[j][i] = t[j][i], t[i][j]


print(t)