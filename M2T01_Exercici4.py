compra = { "Pomes" : {"Qty": 5, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66} }

#Afegeix alguna fruita més

compra['Plàtan'] = {"Qty": 6, "€": 0.88}


#Quant han costat les peres en total?

print("Les peres han costat: " + str(compra['Peres']['€']*compra['Peres']["Qty"]))


#Quantes fruites hem comprat en total?

print("Hem comprat: " + str(compra['Peres']['Qty'] + compra['Pomes']["Qty"] + compra['Plàtan']["Qty"]) + " en total ")


#Quina és la fruita més cara?

mesCar = max(float(d['€']) for d in compra.values())
print("El més car és: " + str(mesCar))