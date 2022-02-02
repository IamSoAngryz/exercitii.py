distanta = 45
pret = 21.22
raining = True
curs = "Python developer"

# array = o secventa de valori de acelasi tip, ordonata si schimbabila.
# list = o colectie ordonata (indexata) de elemente.
# Listele spre deosebire de arrays pot avea elemente de tip diferit.
# Sintaxa de declararea/crearea unuei liste este nume_lista = [elemente_separate_prin_virgula]
numbers = [7, 21, 4, 3, 21, 20] #lista de valori int
cars = ["Sandero 1.4", "VW Golf 6", "Dustrer 4x4"] # lista de strings
prices = [4.56, 5.32, 6.01, 6.14]# lista de valaori float
my_empty_list = [] #empty list
new_numbers = list([7 , 33, 999, 12, 0])
lst = list() # empty list
# index = pozitia in lista, porneste de la 0
# element = item ( valoarea din lista)
# slicing - accesarea unei feliii din lista (osublista respectiv substring)
#sintaxa nume_lista[start:stop:step]
#update list (suprascriere elemente)- [][:] append - la sfarsit insert la index
# ultimele ne elemente folosim lista[len(lista)-n:]
#curs[2] = 'j' String - immutable (nu se pot suprascrie caraterele)
# print('Update de string curs', curs)
# curs = 'Python learning'
# print(curs)
print('Lista numbers', numbers)
removed_value = numbers.pop()
print('Lista numbers dupa stergerea valorii', removed_value,'este', numbers)
removed_from_index_2 = numbers.pop(2)
print('Lista numbers dupa extragerea item cu index 2', removed_from_index_2, 'este', numbers)

del numbers[2]
print ('Lista numbers dupa stergere item cu index 2',numbers)
# del numbers[:2]
# print('Lista numbers, dupa stergere cu del si slicing', numbers)
# del numbers
# print('Lista numbers', numbers)

# numbers.clear()
# print('Lista numbers dupa aplicarea clear:',numbers)
valoarea_de_sters = 7
if  valoarea_de_sters in numbers:
    numbers.remove(valoarea_de_sters)
    print('Lista numbers dupa stergere',valoarea_de_sters, 'este ' ,numbers)
else:
    print(valoarea_de_sters,'nu mai este in numbers')