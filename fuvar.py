#taxi_id;   indulas;               idotartam;    tavolsag;   viteldij;   borravalo;   fizetes_modja
#  0           1                     2              3            4           5             6
#5240;     2016-12-15 23:45:00;    900;          2,5;        10,75;       2,45;        bankkártya

forras=open('fuvar.csv', 'r', encoding='UTF-8-sig')
#lista=[]
fejlec=forras.readline()
#for sor in forras:
 #   lista.append(sor.strip().split(';'))
lista=[sor.strip().replace(',','.').split(';') for sor in forras]
# 3.feladat
print(f'{len(lista)} fuvar')
#4.feladat
bevetel=0
fuvarszam=0
for sor in lista:
    if sor[0]=='6185':
        bevetel=bevetel+float(sor[4])+float(sor[5])
        fuvarszam += 1
print(f'{fuvarszam} fuvar alatt {bevetel}$')
# 5.feladat
# fizmodok=[]
# for sor in lista:
#     fizmod=sor[6]
#     if fizmod not in fizmodok:
#         fizmodok.append(fizmod)
    
fizmodlista=[sor[6] for sor in lista]
fizmodok=set(fizmodlista)
for fizmod in fizmodok:
    darab=fizmodlista.count(fizmod)
    print(fizmod, darab)
    
# 6.feladat
osszestav=0
for sor in lista:
    osszestav+=float(sor[3])
print(f'{osszestav*1.6:.2f} km')

#7.feladat
leghosszabb=0
for sor in lista:
    if int(sor[2])>leghosszabb:
        leghosszabb=int(sor[2])
        taxi_id=sor[0]
        megtettut=sor[3]
        viteldij=sor[4]
print(f'Leghosszabb út: {leghosszabb} másodperc')
print(f'Taxi azonositója: {taxi_id} ')
print(f'Megtett távolság: {megtettut} km')
print(f'Viteldij: {viteldij} $')

# 8.feladat
with open('hibak.txt', 'w',encoding='UTF-8') as hiba:
    print(fejlec)
    for sor in lista:
        if sor[2] and float(sor[4])>0 and float(sor[3])==0:
            print(f'{sor[0]};{sor[1]};{sor[2]};{sor[3]};{sor[4]};{sor[5]}{sor[6]}')
    
    