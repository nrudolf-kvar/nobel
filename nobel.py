# 2. feladat
with open('nobel.csv', encoding='utf-8') as fajl:
    fejlec = fajl.readline().strip('\ufeff\n').split(';')
    nobeldijasok = [nobel.strip().split(';') for nobel in fajl]

# 3. feladat
print(f'3. feladat: {list(filter(lambda x: x[2] == "Arthur B." and x[3] == "McDonald", nobeldijasok))[0][1]}')

# 4. feladat
nev = list(filter(lambda x: x[1] == "irodalmi" and x[0] == "2017", nobeldijasok))
print(f'4. feladat: {nev[0][2]} {nev[0][3]}')

# 5. feladat
szervezet = list(filter(lambda x: x[1] == "béke" and x[0] >= "1990" and x[3] == '', nobeldijasok))
print('5. feladat:')
[print(f'\t{nobel[0]}: {nobel[2]}') for nobel in szervezet]

# 6. feladat
curie = list(filter(lambda x: 'Curie' in x[3], nobeldijasok))
print('6. feladat:')
[print(f'\t{nobel[0]}: {nobel[2]} {nobel[3]}({nobel[1]})') for nobel in curie]

# 7. feladat
stat = {}
for ev, tipus, knev, vnev in nobeldijasok:
    stat[tipus] = stat.get(tipus, 0) + 1
print('7. feladat:')
[print(f'\t{kulcs:<15}{ertek:>20} db') for kulcs, ertek in stat.items()]

# 8. feladat
orvosi = sorted(list(filter(lambda x: x[1] == 'orvosi', nobeldijasok)))
with open('orvosi.txt', 'w', encoding="UTF-8") as fajl:
    [print(f'{nobel[0]}:{nobel[2]} {nobel[3]}', file=fajl) for nobel in orvosi]