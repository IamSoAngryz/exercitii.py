# Code formatting and linting
# Scopul = asigurarea calitatii codului, reability, preventia erorilor
# Linting - analiza codului sursa din punct de vedere stilistic si sintactic
#           evidentiind posibilele probleme
# Linter(lint) = tool(software) care analizeaza codul sursa (stil si sintaxa)
# flake8 - Python linter
# Standardul de calitate = PEP8 (Python Enhancemnet Proposal 8)
# PEP8 = Style guide pt limbajul Python
# autopep8 - formatter pentru python code(standardul pep8)
# instalare - in windows click dreapta document - format document- click pe yes
#               in popup unde se propune instalarea autopep8
# in linux in terminal:     pip install pep8
#                           pip install  - upgrade autopep8
# Windows - adaugare folde in PATH in cmd

number = 77


def max_value(*args):
    """Primeste un numar arbitrar de valori
    Returneaza valoarea maxima
    """
    max = args[0]
    for value in args[1:]:
        if value > max:
            max = value
    return max

def double(v=7):
    return 2*v

print(f'Valoarea maxima este: {max(4, 7, 20, 3, 1, 5, 0,30,5,2)}')
print(f'Valaorea maxima: {max(5, number)}')

curs = 'Python developer'
a, b = 5, 7
double(4)
print(f'Double apelat fara argumente:{double()}')
print(f'Double cu argument: {double(v = 2)}')