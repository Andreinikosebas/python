from operator import itemgetter
n = input()
lista = []
for i in range(n):
    zi, luna = raw_input().split("-")
    zi_nastere = zi, luna
    lista.append(zi_nastere)
lista = sorted(set(lista), key=itemgetter(1,0))
for e in lista:
    print "-".join(e)


