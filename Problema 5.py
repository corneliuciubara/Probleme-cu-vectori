# a)
x=[1,2,3,4,5]
y=[2,4,6,8,10]
suma = 0
for i in range(0,3):
    suma=suma+x[i]
print('Suma primelor 3 numere = ',suma)
# b)
suma = 0
for i in range(0,len(y)):
    suma=suma+y[i]
print('Suma tuturor componentelor variabilei y=',suma)
# c)
produsul = 1
for z in range(0,len(x)):
    produsul=produsul*x[z]
print('Produsul tuturor componentelor=',produsul)
# d)
print('Valoarea absolută a componentei a 3-a',abs(y[3]))
# e)
sum=(x[0]+y[0])
print('Suma primelor componente ale variabilelor x și y',sum)




