 # Functions
 # Functie = o secventa de instructiuni care, atunci cand este apelata, realizeaza un task specific
 # Functii predefinite in Python (build-in) ex print(), len(), input()
 # FUnctii definite de utilizator (user defined)
 
"""
 Sintaxa:
 def nume_functie(parametrii):
     instructiuni
nume_functie - identificator, respecta aceleasi reguli ca numele de variabila
parametri - lista de nume pirn intermediu careia transmitem valori fucntiei(optional)
argumente - valorile efective cu care apelam functia
corpul functiei = secventa de instructiuni prin intermediul careia se realizeaza efectiv taskul
apelare fucntie = punere in executie cu ajutorul numelui functiei ( si parametrii, daca sunt necesari)
return stament = inchide functia( executia functiei) si, optional, returneaza o valoare(Sau mai multe)
documentation string (docstring) - primul rand dupa header(linia cu def) in care descriem ce face functia
Implicit, o functie returneaza None daca nu este specificat altceva prin folosirea retrun
Avantajele folosirii functilor:
- Evita repatarea codului (permit code reuse)
- Permite organizarea codului ( programului ) si impartirea unei probleme de rezolvat mai maari in probleme mai mici
- Permite colaborarea intre programatori atunci cand lucreaza la acelasi produs software
- Adauga claritate codului (reability)
Writing function guidlines
1/ O functie trebuie sa realizeze un singur lucru
2/ Fara duplicari de cod (putem definii functii in cadrul functie sau la acelasi nivel de identare)
3/ numele sa fie descriptiv (cand e necesar adaugam un docstring)
4/ Functia trebuie sa fie simpla , fara cod foarte lung
5/ De preferat, return trebuie sa faca iesirea cu date semnificative intr-un singur loc
"""
def devide(a,b):
    if b !=0:
        rezultat = a / b # return a/b
    else:
        rezultat = 'Impartire la zero' # return 'Impartire la zero'
    return rezultat
print(devide(4, 5))
print(devide(7, 0))
#print("Hello, world")
def hello(name):
    print('Hello,', name)

hello('world')
hello('Iulian')
student = 'Maria'
hello(student)

# Functie care ne returneaza True daca un numar transmis ca parametru este impar, Flase daca nu este
def este_impar(number):
    """Returneaza True daca number este impar, False daca este par"""
    # if number % 2 == 1:
    #     return True
    # else:
    #     return False
    return number % 2 == 1
print('Verificam daca 3 este impar', este_impar(3))
n = 20
print(f' Verificam daca {n} este impar {este_impar(n)}')

def medie(x, y):
    """Returneaza media celor doi parametrii x y"""
    return (x + y) / 2
print(f'Media lui 5 si 6 este {medie(5,6)}')