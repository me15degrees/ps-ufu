#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#
#~# Maria Eduarda Nascimento Andrade ~#
#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#

#variáveis de inicialização recebem valor zero
water, fire, earth, air = 0, 0, 0, 0

while True:
    element = input()
    if element == "X":
        break #se o input for "X" o while é interrompido pelo break

    point = int(input()) #caso não seja "X" ele vai receber um input de tipo inteiro para ser a pontuação
    
    if element == "W":
        water += point #atualiza a pontuação do elemento
        fire -= point/2 #atualiza a pontuação do elemento contrário
        if fire < 0: #caso a atualização leve para um valor negativo, é preciso corrigir
            fire = 0
    
    elif element == "F":
        fire += point
        water -= point/2
        if water < 0: 
            water = 0
    
    elif element == "E":
        earth += point 
        air -= point/2 
        if air < 0: 
            air = 0    
    
    else: 
        element == "A"
        air += point 
        earth -= point/2 
        if earth < 0:
            earth = 0

print("Pontuacao Final")
print(f"Agua: {water:.1f}")
print(f"Terra: {earth:.1f}")
print(f"Fogo: {fire:.1f}")
print(f"Ar: {air:.1f}")

need_more_training = False

#valida se precisa de mais treinamento
if not all([water, fire, earth, air]):
    need_more_training = True

#print final
if need_more_training:
    print("Realize mais treinamentos.")
else:
    print("Treinamento realizado com sucesso.")