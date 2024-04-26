# Ex 62 Melhorar o Ex 61 perguntando se quer mostrar mais termos
#   o programa encerra quando o usuário disser 0 termos.

primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))

a = 1
contador = 0
while a <= 10:
    print('\033[31m', primeiro_termo, end='\033[34m → \033[34m')
    primeiro_termo += razão
    a += 1
    contador += 1

# a = 11 aqui

print('\033[1;33m PAUSA \033[m')


escolha = 1
while escolha != 0:
    escolha = int(input('\033[32mQuantos termos você quer mostrar a mais? (Digite 0 para encerrar)\n\033[m'))
    a = 1
    while a <= escolha:
        print('\033[31m', primeiro_termo, end='\033[34m → \033[34m')
        primeiro_termo += razão
        a += 1
        contador += 1
print(f'\033[33mA PA acabou com {contador} números mostrados.\033[m')

# Método Guanabara

print(' ')
print('\033[1;34m↓↑\033[m' * 30)
print('\033[1;36m↓↑\033[m' * 30)
print(' ')
print('\033[1;32m----Método Guanabara----\033[m')

primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
contador = 1
escolha = 10
total = 0
while escolha != 0:
    total += escolha # Total = 10 aqui
    while contador <= total:
        print('\033[31m', primeiro_termo, end='\033[34m → \033[34m')
        primeiro_termo += razão
        contador += 1
    print('\033[1;33m PAUSA \033[m')
    
    escolha = int(input('\033[32mQuantos termos você quer mostrar a mais? (Digite 0 para encerrar)\n\033[m'))

print(f'\033[33mA PA acabou com {total} números mostrados.\033[m')
print('\033[1;33m FIM! \033[m')
