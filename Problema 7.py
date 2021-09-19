Zi = ['Luni','Marți','Miercuri','Joi','Vineri','Sîmbătă','Duminică']
v = [100,99,102,101,103,98,101]
# a)
suma = 0
for i in range(0,len(v)):
    suma=suma+v[i]
print('Venitul săptămînal =',suma)
# b)
media = suma/len(v)
print('Media venitului',media)
# c)
print('Ziua cu cel mai mare venit=',Zi[v.index(max(v))])
# d)
print('Ziua cu cel mai mic venit=',Zi[v.index(min(v))])