from math import sqrt
x = input()

radacina = int(sqrt(x))

if radacina % 2 == 0:
    print "Radacina e para ---> trans intr-o rad impara!"
    radacina -= 1
else:
    print "Radacina este impara!"

rest = x - radacina**2
print "Restul este: ", rest

