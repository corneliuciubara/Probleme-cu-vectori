Ora = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
t = [-20,-18,-17,-16,-15,-14,-13,-10,-6,-4,0,2,3,4,5,6.5,7,6,5,4,0,-5,-10,-18]
# a)
suma = 0
for i in range(0,len(t)):
    suma=suma+t[i]
    media= suma/len(t)
print('temperatura medie',media)
# b)
print('Maximul temperaturii =',max(t))
print('Minimul temperaturii = ',min(t))
# c)
print('Ora la care s-a înregistrat temperatura maximă este ora',Ora[t.index(max(t))])
# d)
print('Ora la care s-a înregistrat temperatura minimă este ora',Ora[t.index(min(t))])
# e)
cntNEG = 0
for i in range(0,len(t)):
    if (t[i]<0):
        cntNEG+=1
        print('Numărul de înregistrări negative',cntNEG)
# f)
cntM = 0
for i in range(0,len(t)):
    if(t[i]>media):
        cntM+=1
    print('Numărul de înregistrări > media',cntM)



