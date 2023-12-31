#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#
#~# Maria Eduarda Nascimento Andrade ~#
#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#

"""d1 = pessoas imunizadas com apenas uma dose, estando a segunda atrasada ou não
d2 = pessoas completamente imunizadas
d1a = pessoas que tomaram a primeira e esperam a segunda dose com atraso
d2a = pessoas que tomaram a segunda dose com atraso"""

d1, d2, d1a, d2a = 0,0,0,0

n = int(input()) # recebe o valor de meses que serão analisados
i = 0 # contador

while i < n:
    vacinas = int(input())
   
    if d1a:
        while vacinas and d1a:
            vacinas -= 1 # vai subtraindo as vacinas
            d1a -= 1 # menos uma pessoa aguardando a segunda dose em atraso
            d2a += 1 # mais uma pessoa que tomou a segunda dose em atraso
            d2 += 1 # mais uma pessoa completamente imunizada
    if d1: # pessoas que tomaram a primeira dose, mas que ainda não estão atrasadas
        while vacinas and d1:
            vacinas -= 1
            d1 -= 1 # menos uma pessoa aguardando a segunda dose
            d2 += 1 # mais uma pessoa completamente imunizada
        if d1: # significa que as vacinas acabaram mas o d1 não, logo elas vão ser pessoas d1a
            d1a += d1 # agora elas estão esperando a segunda dose em atraso
            d1 = 0 # não temos mais pessoas regulares
    if vacinas:
        d1 += vacinas # assim que eu recebo mais dose eu faço a primeira dose das outras pessoas
    i += 1     

print("Pessoas completamente imunizadas:",d2)
print("Pessoas imunizadas apenas com uma dose:",d1+d1a)
print("Pessoas que tomaram a segunda dose com atraso:",d2a)
print("Pessoas esperando a segunda dose com atraso:",d1a)