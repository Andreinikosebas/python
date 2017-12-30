from itertools import cycle

text = raw_input()
nr_chei = input()
text_criptat = ''
nr = 0
lista_chei = []
litere_mari = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
litere_mici = ('abcdefghijklmnopqrstuvwxyz')

for i in range(nr_chei):
    lista_chei.append(input())

for ch in text:
    pozitie = 0
    if ch in litere_mari:
        pozitie = lista_chei[nr%len(lista_chei)] + litere_mari.index(ch)
        text_criptat = text_criptat + litere_mari[pozitie%len(litere_mari)]
        nr += 1
    elif ch in litere_mici:
        pozitie = lista_chei[nr%len(lista_chei)] + litere_mici.index(ch)
        text_criptat = text_criptat + litere_mici[pozitie%len(litere_mici)]
        nr += 1
    else:
        text_criptat = text_criptat + ch

print text_criptat





