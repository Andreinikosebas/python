m = input()
n = input()
v1 = []
v2 = []
for elemente in range(n*m):
    v1.append(input())
v3 = set(v1)
for i in v3:
    v2.append(i)
    v2.append(v1.count(i))
dif = len(v1) - len(v2)
print dif




