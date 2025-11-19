# II.
# Olvassunk be billentyűzetről tizedes törteket (float), és tároljuk őket egy listában!
# A bevitel végét a 0.0 jelzi.
# Majd oldjuk meg a következő feladatokat!
# Minden feladat előtt a program írja ki a feladat sorszámát!

# 1. Volt-e 5.5-nél nagyobb szám a listában?
# 2. Írjuk ki az első olyan szám indexét, ami negatív és egész (pl.: -2.0, -5.0)!
# 3. Hány darab 1 és 2 közé eső szám szerepel a listában?
# 4. Melyik volt a legnagyobb értékű negatív szám, és hányadik helyen állt?
# 5. Mennyi a pozitív számok összege?

tizedes_tort_lista = []
egy_ketto_kozott = []
negativ_szamok = []

while True:
    tizedes_tort = float(input('Adj meg egy tizedes törtet: '))
    tizedes_tort_lista.append(tizedes_tort)
    valasz = input('Akarsz még hozzá adni a listához. (y/n)')
    if valasz == 'y':
        continue
    else:
        break




print('1. feladat')

if any(szam > 5.5 for szam in tizedes_tort_lista):
    print('Volt 5.5-nél nagyobb szám a listában.')

else:
    print('Nem volt 5.5-nél nagyobb szám a listában.')

print('-----------------------\n')




print('2. feladat')

talalt = False

for szam in tizedes_tort_lista:
    if szam.is_integer() and szam < 0:
        print(f'Ez az első negatív egész szám indexe: {tizedes_tort_lista.index(szam)}')
        talalt = True
        break

if not talalt:
    print('Nincsen negatív egész szám a listában.')

print('-----------------------\n')




print('3. feladat')

for szam in tizedes_tort_lista:
    if szam < 2 and szam > 1:
        egy_ketto_kozott.append(szam)

if len(egy_ketto_kozott) > 0:
    print(f'{len(egy_ketto_kozott)} db szám volt ami 1 és 2 között van')

else:
    print('Nincsen szám 1 és 2 között.')

print('-----------------------\n')




print('4. feladat')

for szam in tizedes_tort_lista:
    if szam < 0:
        negativ_szamok.append(szam)

if len(negativ_szamok) > 0:
    print(f'Ez volt a negatív számok között a legnagyobb: {max(negativ_szamok)}')
    max_negativ = max(negativ_szamok)
    print(f'Ezen a helyen állt: {tizedes_tort_lista.index(max_negativ)}')

else:
    print('Nem volt a listában negatív szám.')

print('-----------------------\n')




print('5. feladat')

pozitiv_szamok = 0

for szam in tizedes_tort_lista:
    if szam > 0:
        pozitiv_szamok += szam

if pozitiv_szamok > 0:
    print(f'Pozitív számok összege {pozitiv_szamok}')

else:
    print('Nincsenek pozitív számok a listában.')

print('-----------------------\n')
