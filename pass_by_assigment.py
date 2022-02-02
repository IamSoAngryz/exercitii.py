# Passing arguments to function by assigment
# 1/Argumentele sun varaibila de tip immutable (str, int, float, bool) la assigment in interiorul functiei se crreeaza o varabila locala
# Daca vrem sa modificam valaorea argumentelor, folosim return si assigment pt a reflecta modificarile in program
# 2/ Argumentele sunt mutable(schimbabile in-place, se pot rescrie items, de exp list) - la assigment in interiorul functiei se creeaza tot variabila locala
# 2.1/ Argumentele mutable se pot "modifica" daca le returnam si asignam noua valoare intoarsa, similiar cu 1/
# 2.2/ Argumentele mutable, daca se modifica in-place(append, assigment pe baza de index, insert, etc), daca suprascriem un item sau inserma unul(operatii de mutare)
# se realizaeza "pass by assigment" in sensul ca modificarea va fi reflectata in program fara a se folosii return

# Pass by assigment inseamna ca argumentele se vor comporta diferit in functie de tipul lor
# Cand folosim argumente mutable si suprascriem elemente (schimbam/mutam argumentul in interiorul functiei) - schimbarea se reflecta dupa finalizarea functiei in program
# Mecanismul este similar cu "Pass by reference" din alte limbaje de programare
# Un al doilea mecanims de transmitere a argumentelor este "Pass by value" relativ simulat cand realizam assigment in interiorul functiei (atat pt mutable cat si pt immutable data)
# Pass by assigment functioneaza pt ca Python creeaza variabile ca referinte pt obiecte(=reprezentari concrete ale unor tipuri de date)
# Este esential daca acele obiecte sunt sau nu mutable pt a determina daca modificarile(mutarile) se reflecta in afara functiei asupra argumentelor transmise

# Modificarile elemtelor listelor transmise ca argumente functilor,se reflecta in afar functiei fara sa fie necesar return
# Modificarile oricarui tip de argumente se pot reflecta prin return si assigment

x = 7
gl = ['old', 6, 20]

def double(number):
    """Dubleaza valaorea parametrului number"""
    number *=2 # se creeaza o variabila locala
    return number

def f(my_list):
    my_list = [3, 5] # se creeaza o variabila locala
    print(f'Lista din interiorul fucntiei f este {my_list}')
    return my_list

def g(lst):
    lst[0] = 'new'
    lst[1]+=1
    lst.append(77)
    print(f'Lista din interiorul functiei {lst}')

x = double(x)
print(f'Dublul lui x este {x}')


l =[6, 7]
print(f'Lista l inainte de executia functiei f: {l}')
f(1)
print(f'Lista l dupa executia functiei f: {l}')

print()
print(f'Lista gl inaitne de executia functiei g {gl}')
g(gl)
print(f'Lista gl dupa executia functiei g: {gl}')