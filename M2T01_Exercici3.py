import random
lista= []
i = 0
while i<=49:
    lista.append(random.randint(0,49))
    i += 1

#Quants números hi ha?
len(lista)
print('Hi han '+ str(len(lista)))


#Quantes vegades apareix el número 3.

total_3=0
for j in range(0, len(lista)):
    if lista[j] == 3:
        total_3 +=1

print('El 3 apareix un total de ' + str(total_3)+ " vegades")

#Quantes vegades apareixen els nombres 3 i 4?

total_3=0
total_4=0
for j in range(0, len(lista)):
    if lista[j] == 3:
        total_3 +=1
    elif lista[j] == 4:
        total_4 += 1

total= total_3+total_4
print('El 3 i el 4 apareixen un total de ' + str(total)+ ' vegades')

#Quin és el número més gran?

print('El número més gran es ' + str(max(lista)))

#Quins són els 3 números més petits?

lista1 = [*set(lista)]
print('Els 3 números més perits són ' + str(lista1[0:3]))


#Quin és el rang d’aquesta llista?


print("El rang és : " + str(min(lista)) + "-----" + str(max(lista)))


