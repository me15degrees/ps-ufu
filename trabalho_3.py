#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#
#~# Maria Eduarda Nascimento Andrade ~#
#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#

#recebe do usuário as variáveis float
a = float(input())
b = float(input())
c = float(input())

#faz o cálculo do delta
delta = b ** 2 - (4 * a * c)

if a == 0 or delta < 0: #descarta configurações da expressão que não funcionam
     print("Impossivel calcular")

elif delta == 0: #calcula R1 dada a condição de delta igual a zero
    x1 = (-b + delta**0.5) / (2 * a)
    print(f"R1 = {x1:.5f}")

else: #calcula R1 e R2 dada a condição que delta maior que zero
    x1 = (-b + delta**0.5)/(2 * a)
    x2 = (-b - delta**0.5)/(2 * a)
    print(f"R1 = {x1:.5f}") 
    print(f"R2 = {x2:.5f}")