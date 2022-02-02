# Casting ( Type Casting) = conversia de tip aplicata unei varibile sau unui literal
# int/ floar / str ex. str(2)
pret_unitar = '24.50'
numar_unitati = 7
pret_total = float(pret_unitar) * numar_unitati
print('Prestul total este', pret_total)

# input = citim date de la tastatura
pret_unitar_citit = input('Introduceti pretul')
#print(type(pret_unitar_citit))
print('Pret total pe baza pretului citit de la tastatura este',float(pret_unitar_citit)*numar_unitati)