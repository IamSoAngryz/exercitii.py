# Global in nested functions
# global nume_varaibila in nested functions pt a extinde veraible scope ( scopul variabilei) la nivel global
# folosind global, modificarile efectuate in functia inclusa se refelcta in program (main) la nivel global

# nonlocal - extinde domeniul de vizibilitate al unei variabile de la functia in care este definita la functia la care cuprinde acea functie, 
# situatia valabila doar in cazul nested functions.

x = 2 # global variable
y = 100 # global variable

def f():
    x = 3 # variabila locala
    print(f'Variabila x din interiorul f: {x}')
    def f2():# nested functions
        global x # domeniu de vizibilitate este extins la global scope
        x= 4 #variabila globala
        print(f'Varabila x din interiorul f2: {x}')
    f2()
    print(f'Variabila x dupa executia f2 in interiorul f: {x}') # x: 3 *variabila locala


def g(): # enclosing functions( g include g2)
    y = 10 # variabila locala
    print(f'Variabila y din interiorul g: {y}')
    def g2():
        nonlocal y
        y = 20 #variabila nonlocal, scope-ul este extins la nivelul functiei g
        print(f'Variabila y din interorul g2: {y}')
    g2()
    print(f'Variabila y din interiorul g, dupa executia g2: {y}')
print(f'Variabila x inainte de executia fucntiei f: {x}')
f()
print(f'Variabila x dupa executia functiei f: {x}') # x: 4
print()
print(f'Variabila y inainte de executia g: {y}')
g()
print(f'Variabila y dupa executia g: {y}')