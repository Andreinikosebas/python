x = raw_input()
lista = []
for i in x:
    lista.append(int(i))

pas = len(lista)/2
suma = 0

for i in range(len(lista)):
    if lista[i] == lista[(i+pas)%len(lista)]:
        suma += lista[i]

print suma
