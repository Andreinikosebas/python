from math import sqrt
n = input()
nr = 0
valori = [float(i) for i in raw_input().split()]
R = sum(valori)/n
patrate = [(i-R)**2 for i in valori]
S = sqrt(sum(patrate)/n)
for i in valori:
    if i >= R-S and i <= R+S:
        nr += 1
rezultat = float(nr)/n*100
print "%.2f" % rezultat


