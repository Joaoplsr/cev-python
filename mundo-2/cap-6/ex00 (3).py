# Ex 58 Melhorar o desafio 28(0,10), só que agora o jogador tenta até acertar.
#   O jogo deve mostrar quantos palpites ele deu.

from random import randint


print('-=-' * 20)
print('Eu pensei em um número entre 0 e 10. \033[35mVocê jamais advinharia!\033[m')
print('-=-' * 20)
num = randint(0,10)
palpites = 1
totpalpites = 0
num = str(num)
chute = ''
while chute != num:
    chute = str(input(f'\033[36mChute {palpites}: \033[m')).strip()
    palpites += 1
    totpalpites += 1
    if chute < num:
        print('\033[31mMais... Tente novamente!\033[m')
    elif chute > num:
        print('\033[31mMenos... Tente novamente!\033[m')
print(f'\033[32mVocê acertou em {totpalpites} palpites!\033[m')
print(f'\033[34mO número correto era {num}.\033[m')

print('Método Guanabara')

# Método Guanabara
p = 0
computador = randint(0, 10)
print('Pensei em um número entre 0 e 10, você consegue acertar?')
acertou = False
while not acertou:
    jogador = int(input('Dê seu palpite: '))
    p += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('Um pouco mais... Tente novamente.')
    else:
        print('Um pouco menos... Tente novamente.')
print(f'Você acertou com {p} tentativas.')

    