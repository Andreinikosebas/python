y = []
x = raw_input().split()
for i in x:
    y.append(int(i))

valori = []

count = 0
L = len(y)
while y not in valori:
    valori.append(list(y))
    count += 1
    m = max(y)
    loc = y.index(m)
    y[loc] = 0
    for i in range(m):
        loc += 1
        y[loc%L] += 1

print count
