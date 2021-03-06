#Substrings, comparing strings
curs = 'Python Developer'
job = 'Developer'
second_job = 'developer'
name ='Python'
lang = 'Python'
print('Verificam daca doua stringuri sunt egale', name == lang)
print('Comparam alte doua stringuri', job != second_job)

# verificam daca un string este substring (inclus in alt string)
if name in curs:
    print(name, 'este in', curs)
else:
    print(name, ' nu este in', curs)
string_inclus = curs[:6]
print('Substringul din stringul curs obtinut prin slicing', string_inclus)
if string_inclus == name:
    print('Stringul',curs,'incepe cu' ,name)
else:
    print('Stringul', curs, 'nu contine la inceput', name)
# Folosim slincing si len pt a determina daca un string este substring in altu
if curs[:len(name)] == name:
    print('Stringul', name,'este sustring a lui', curs)


# Functia startswith() - determian daca un string  incepe cu altu
# sintaxa: string.startswith(string2)
print('Verificam daca',second_job, 'este substring al',curs,':',curs.startswith(second_job))
print('Verificam daca stringul',curs,'se termina cu',lang,':', curs.endswith(lang))

#Spatiile schimba rezultatul evaluarii, strip()-elimina spatii de la inceput si sfarsit
print('Stringul     acesta are spatii la inceput si sfarsit    '.strip()+'Le-am eliminat')

# find() cauta u nsubstring si returneaza pozitia la care e gasit (sau -1 daca nu este inclus)
print('Pozitia la care se gaseste', job, 'in',curs,'este:',curs.find(job))
print('Pozitia la care se gaseste', second_job, 'in',curs,'este:',curs.find(second_job))