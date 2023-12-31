#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#
#~# Maria Eduarda Nascimento Andrade ~#
#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#

N = int(input())
if 0 <= N <= 10000000:
    D = N // (3600*24)
    H = N // 3600 % 24
    M = N % 3600 // 60
    S = N % 3600 % 60
    print(D, "dia(s),", H, "hora(s),", M, "minuto(s) e", S, "segundo(s).") 