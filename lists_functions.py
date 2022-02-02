# Bult-in list functions
#count() - returneaza numarul de aparitii pt o valoare
numbers = [4, 6, 33, 2, 44, 5, 6, 0, 6, 4, 1]
print('Lista numbers', numbers)
valoare = 6
print('Valoarea', valoare,'apare de',numbers.count(valoare),'ori')

# sort() - sorteaza elementele unei liste
numbers.sort()
print('Lista numbers sortata:', numbers)
print('Rezultatul cautarii valorii 77 in lista numbers este',numbers.count(77), 'ori')
if 77 not in numbers:
    print('Valoarea 77 nu este prezenta in lista numbers')
# max - determina valoarea maxima din lista
print('Maximul din lista numbers:',max(numbers))
#min - determina valoarea minima din lista
print('Valoarea minima din lista numbers', min(numbers))

# in Python Shell folosim helpul iteractiv 
# dir(list) sau dir([]) sau dir(variabila_tip_lista) -toate functile pt tipul de date
# help(list.nume_functie) - instructiuni de utilizare a functilor
# help([5].nume_functie)
# help(len), help(max) - help Python pentru functile len sau max