# Ternary if- else operator
# value_tru if condition else value_false

numar = 7 
paritate = 'par' if numar %2 ==0 else ' impar'
print('Numarul', numar, 'este', paritate) 

pret_maxim_de_achizitie = 30
pret_actual = 40
print('Achizitia este apropbata'if pret_actual<=pret_maxim_de_achizitie else 'Achizitia este suspendata')