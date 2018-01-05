n, k = map(int, raw_input().split())
valori = map(int, raw_input().split())
valori_strigate = map(int, raw_input().split())
#if set(valori).issubset(valori_strigate):
#    print "BINGO!"
#else:
    #print len(set(valori) - set(valori_strigate))

#Varianta 2:
if all(i in valori_strigate for i in valori):
    print "BINGO!"
else:
    print len(set(valori) - set(valori_strigate))