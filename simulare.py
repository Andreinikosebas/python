HH,MM = map(int, raw_input().split(":"))
N = int(raw_input())

list_of_lists = []

for i in range(N):
    list = []
    TMT,NR,TA,DC = map(str, raw_input().split(" "))
    NR = int(NR)
    TA = int(TA)
    DC = int(DC)
    total_time = TA + DC
    list.append(TMT)
    list.append(NR)
    list.append(total_time)
    list_of_lists.append(list)

a = min(map(lambda x: x[2], list_of_lists))
print(a)
lista = []
for j in list_of_lists:
    for e in j:
        if a == e:
            HH = HH + (MM + a) / 60
            MM = (MM + a) % 60
            print("%s %d %02d:%02d" % (j[0], j[1], HH, MM))





