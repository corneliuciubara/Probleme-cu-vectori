x=[1,2,3,4,5]
y=x.copy(x)
suma = 0
for i in range(0,2):
    suma=suma+x[i]
print('Suma primelor 3 elemente din x =',suma)
sumay = 0
for z in range(0,len(y)):
    sumay=sumay+y[z]
print('Suma primelor 3 elemente din y =',sumay)
produs = 1
for i in range(0,len(x)):
    suma=suma*x[i]
print('Suma primelor 3 elemente din x =',produs)
print(sum(x[0]+y[0]))

