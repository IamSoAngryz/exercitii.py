# python keywords = cuvinte cheie, rezervate, care au un sens si un scop specific in Python
# Nu putem folosii keyword la declararea variabilelor sau la definirea functilor
# help('keywords')
# None - nicio valoarea (echivalentul lui null, undefined din alte limbaje)
# truthiness (veridicitate) - evaluarea expresilor ijn context boolean
# False rezulta si in urma evaluarii unei expresii [], '', "", 0
# expresile empty sunt evaluate in context boolean la False
help('keywords')

def este_impar(number):
    return number % 2 == 1

def continue_op(number):
    pass

def salut():
    print('Salut')
    # return x

def imparte(x, y):
    if y!= 0:
        return x / y
    # else:
    #     return

salut()
# print(salut()) # returneaza None
rezultat = salut()
print(f'Rezultatul intors de functia salut este {rezultat}')
print(f'Type de None {type(None)}')
# if rezultat is None - testam daca o fucntie a returnat un rezultat explicit sau cel Default
print(imparte(4, 5))
print(imparte(4, 0)) # None e returnat cand functia nu specifica alt return explicit
#bool() - evalueazai n context boolean o expresie
print(f'Evaluand list [4, 5] in context boolean obtinem {bool([4, 5])}')

if 4>0:
    print('4 este mai mare ca zero')
    print(4>0)

numbers = []
if 40 > 20:
    numbers.append(55)
if numbers: # Python evalueaza in context boolean si o lista, este Flase daca este [] si True altfel
    print('Am adaugat un element')

value = imparte(6, 0)
if value is None:
    print('Impartire la zero!')