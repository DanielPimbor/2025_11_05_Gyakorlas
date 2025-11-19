# I.
# Szimuláljuk egy 6 oldalú kocka 20 dobását! A dobásokat egy listában tároljuk!
# Majd oldjuk meg a következő feladatokat!
# Minden feladat előtt a program írja ki a feladat sorszámát!

# 1. Volt-e 5-ös dobás a listában?
# 2. Hanyadik dobás lett először 1-es?
# 3. Hány darab páros számot dobtunk?
# 4. Melyik volt a legkisebb dobás a 4-nél nagyobbak közül, és hányadik dobás volt?
# 5. Mennyi a 3-as dobások összege?

import random

dobasok_szamai= []
paros_szamok = []
negynel_nagyobb_szamok = []
harmas_dobasok = []

for i in range(21):
    i = random.randint(1,6)
    dobasok_szamai.append(i)

print(dobasok_szamai)




print('1. feladat')

if 5 in dobasok_szamai:
    print('Volt 5 benne.')

else:
    print('Nincs 5-ös a listában.')

print('-----------------------\n')




print('2. feladat')

if 1 in dobasok_szamai:
    index = dobasok_szamai.index(1)
    print(f'A {index + 1}-edik dobás lett 1.')

else:
    print('Nincs 1-es a listában.')

print('-----------------------\n')




print('3. feladat')

for szam in dobasok_szamai:
    if szam % 2 == 0:
        paros_szamok.append(szam)

if len(paros_szamok) > 0:
    print(f'{len(paros_szamok)} a páros számok száma.')

else:
    print('Nincs páros szám a listában.')

print('-----------------------\n')




print('4. feladat')

for szam in dobasok_szamai:
    if szam > 4:
        negynel_nagyobb_szamok.append(szam)

if len(negynel_nagyobb_szamok) > 0:
    print(f'Ez volt a legkisebb a négynél nagyobbak közül: {min(negynel_nagyobb_szamok)}')
    print(f'Ehanyadik dobás volt: {(dobasok_szamai.index(min(negynel_nagyobb_szamok))) + 1}')

else:
    print('Nincs 4-nél nagyobb szám a listában.')

print('-----------------------\n')




print('5. feladat')

if 3 in dobasok_szamai:
    for szam in dobasok_szamai:
        if szam == 3:
            harmas_dobasok.append(szam)
            harmas_dobasok_osszege = len(harmas_dobasok) * 3
    print(f'Ennyi hármas volt: {len(harmas_dobasok)}')
    print(f'A hármas dobások összege: {harmas_dobasok_osszege}')

else:
    print('Nincs 3-as a listában.')

print('-----------------------\n')




