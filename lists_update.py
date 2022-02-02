distanta = 45
pret = 21.22
raining = True
curs = "Python developer"


# array = o secventa de valori de acelasi tip, ordonata si schimbabila.
# list = colectie ordonata( indexata ) de elemente
# Listele spre deosebire de arrays pot avea elemente de tip diferit.
# Sintaxa de declarea/ crearea unei liste este nume_lista = [elemente_separate_prin_virgula]
numbers =[7, 21, 4, 3, 21, 20] #lista de valori int
cars = ["Sandero 1.4", "vW Golf 6", "Duster 4x4"] # lista de strings
prices = [4.56, 5.32, 6.01, 6.14] #lista de valori float
my_empty_list = [] #empty list
new_numbers = list([7,33, 999, 12, 0])

# index = pozitia in lista, porneste de la 0
# element = item (valoare din lista)
#print('Pretul cu index 10 ', prices[10])
# list si str au in comun indexul (accesare element de baza), len - determina lungimea
#list - mutable (schimbabile putem suprascire valorile items) strings -imutable
# list si str sunt iterables (iterabile, pot fi parcurse elemente unul cate unul intr-un for)
#negative indexes - elemente de la sfarstiul listei cand nu ii stim lungimea
#update list  (suprascriere elemente ) - [] [:] append - la sfarsti si insert la un index
#curs[2] = 'j' String  - imutable ( nu se poate suprascrie caractere)
# print('Update string curs', curs)
# curs = 'Python learining'
# print(curs)
# list - mutable (schimbabile)
print('Lista numbers', numbers)
numbers[2] = 77
print('Lista numbers, dupa suprascriere item cu index 2',numbers)
#curs[2] = 'j' String - immutable (nu se pot suprascrie caractere)
# print('Uptade string curs', curs)
# curs = 'Python learning'
# print(curs)
numbers[2:4] = [0, -3]
print('Lista numbers dupa update aplicand slicing operator',numbers)

numbers.append(121)
print('Lista dupa append', numbers)
numbers.insert(2, 3233)
print('Lista numbers dupa insert in pozitia 2',numbers)