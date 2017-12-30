n = input()
sir = []
nr = 0
start = 0
test = []
lista_perechi = []
pereche = []
final = []

for i in range(n):
    sir.append(input())
sir1 = sir

for val in sir:

    if val >= 0:
        pereche.append(val)
    elif len(pereche) > 0 and val < 0:
        lista_perechi.append(pereche)
        pereche = []
    else:
        test.append(val)
    sir.remove(val)
print "Lista de perechi pozitive este: ", lista_perechi
print "sirul cu nr negative: ", test

#a = max(map(lambda x: len(x), lista_perechi))
#print a
#if len(test) == len(sir):
#    print "-1", 0
#else:
#    for x in lista_perechi:
#        if a == len(x):
#            final.append(x)
#    if len(final) == 1:
#        print sir.index(final[0][0])
#        print len(final[0])
#    else:
#        print "bag pl nush sa fac!"
#print final







