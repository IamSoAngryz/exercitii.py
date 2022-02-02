def este_impar(number):
    if number % 2 == 1:
        return True
    else:
        return False
print('Verificam daca 3 este impar',este_impar(3))
n = 20
print(f'Verificam daca {n} este impar {este_impar(20)}')

def hello(name):
    print('Hello', name)

hello('world')
hello('Marian')
nume = 'Bogdan'
hello(nume)


def medie(x, y):
    return (x + y) /2
print(f'Media lui 5 si 6 este {medie(5,6)}')

def medie(a, b):
    return (a-b)*2
print(f'Media lui 10 si 2 este {medie(10,2)}')

def medie(z, o):
    return (z - o)*3
print(f'Media lui 10 si 20 este {medie(10,20)}')

def medie(i, s):
    return(i + s)*4
print(f'Media lui 10 si 20 este {medie(10,20)}')

def f(a, b=10):
    print('a+2*b=', a+2*b)
f(6) # apelam functia

x = 7
def add():
    global x
    x += 7
print(f'Variabila x inainte de apelarea functie add: {x}')
add()
print(f'Variabila x dupa apelarea functiei add: {x}')

curs = "Python developer"
student = "Domnit Bogdan"
def show_language(nume_curs):
    curs = 'Java developer'
    words = nume_curs.split()
    language = words[0]
    print(f'Language for {nume_curs} is {language}')
    print(f'Afisam variabila locala din functia show_language {student}')
    print(f'{curs}')
show_language(nume_curs=curs)

list1 = [0, 1, 4, 5]
list2 = [20, 15, 3, 10]

list3 = list1+list2
print(list3)