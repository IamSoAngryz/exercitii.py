# Passing primitive variables to functions at parameters
# Primitive variables = variabile de tipuri de baza(int, float, str, boolean)
# basic data types variable (variabile cu date de baza, primitive:int ,str, float, boolean)- sunt immutable
# o functie poate modifica o variabila avand tip immutable doar daca o intoarce prin return
# PRin return putem intoarce mai multe variabile
number = 4
v1 = 7
v2 = 2
 
def square(x):
     """Ridica x la patrat"""
     x = x **2 #x = x*x x- local varaible
     print(f'x in interiorul functiei {x}')
     return x

def cat_rest(a, b):
    """ Calculeaza catul si restul impartirii celor doi parametrii intrgi
    Returneaza catul si restul
    """
    cat = a // b
    rest = a % b
    return cat, rest

def create_name(nume, prenume):
    nume  = nume + ' '+ prenume # full_name =' '.join(nume, prenume)
    return nume

number = square(number)  # transmitem ca argument un int functiei square
print(f'Valaorea lui numbers la patrat {number}')

c, r = cat_rest(v1, v2) # putem prealua prin enumerare rezultatele multiple ale unei functii
print(f'Catul este {c} si restul este {r}')
nume, prenume, g = "Domnit","Bogdan", 789
print(f'Nume= {nume} si prenume = {prenume}')
print(g)

new_name = create_name("Alex", "Dobre")
print(f'Nume intreg = {new_name}')