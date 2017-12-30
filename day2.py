#n = raw_input().split('\n')
#x = []
#lista = []
#for j in n:
#    x = j.split()
#    for i in range(len(x)):
#        x[i] = int(x[i])
#    print max(x)

x = []
suma = 0

while True:
    try:
        x.append(raw_input())
    except EOFError:
        break
n = []
nr = 0
for i in x:
    nr += 1
    n = i.split()
    vector = []
    for j in n:
        vector.append(int(j))
    for k in vector:
        for l in vector:

            if l % k == 0 and l != k:
                print "Pentru linia %d nr divizibile sunt %d si %d" %(nr, l, k)
                suma += (l / k)
                print "Suma a crescut la %d" % suma
            #elif k % l == 0:
             #   print "Pentru linia %d nr divizibile sunt %d si %d" % (nr, k, l)
              #  suma += (k / l)
               # print "Suma a crescut la %d" % suma
print suma