# Version control = controlul versiunilor (reviziilor) unui software
# Version control sistem (VCS) = un sistem de versionare
# - urmareste si stocheaza schimbarile unui cod sursa
"""
Avantaje folosirii VCS:
1. un istoric comple al fiecarui fisier in parte (permite revenirea la o versiune anterioara oricand si fixarea unor erori)
2. cand mai multi developeri lucreaza la un proiect pot lucra pe fluxuri separate numite branches si pot aduce la final rezultatul in proiect
3. intotdeauna cea mai recenta versiunea e accesibila tuturor developeri
4. daca folosim un serviciu de hosting dedicat VCS, avem permant un backup(copie de siguranta)

"""



"""Doua tipuri de VCS
1. Centralizat (CVCS)- tine o copie centrala a proiectului pe un server central
    1.1 un developer isi trage si are acces doar la fisierele care lucreaza
    1.2 niciodta un developer nu are acces la tot proiectul
2. Distribuit (DVCS):
    2.1 nu exita obligatoriu un server central care sa stocheze toate versiunile
    2.2 fiecare developer are acces la intreg proiectul si la istoricul modificarilor
    2.3 copiaza (cloneaza) local intreg priectul cu istoric
    2.4 pentru colaborare, cea mai recenta versiune este tinuta online, 
        cu ajutorul unui serviciu de gazduire dedicat VCS
    Proiectul si istoricul modificarilor = repository
    Fiecare schimbare salvata = commit

"""