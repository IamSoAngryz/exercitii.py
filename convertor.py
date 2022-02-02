# Realizeaza conversia unor sume in dolari si euro la cursul zilei
sume = ['100$', '20E', '33$', '44.20E']
rata_conversie_dolar_leu = 4.1
rata_conversie_euro_leu = 4.9
sume_num = [float(x[:-1])*rata_conversie_dolar_leu if x[-1]== '$' else float(x[:-1])* rata_conversie_euro_leu for x in sume]
print(f'Sumele initiale: {sume}')
print(f'Sume in lei: {sume_num}')
# for suma in sume_num:
#     print(f'Suma este {suma:.2f}')
print('Sumele in lei:', end= ' ')
[print(f'{suma:.2f}', end = ' ')for suma in sume_num]
print()
