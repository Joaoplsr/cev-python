# Ex 45 Jokenpô contra PC

print('\033[1;31m♦♣♠♥\033[m' * 6)
print('\033[1;31m♦\033[m', ' ' * 6, '\033[1;33mJOKENPÔ\033[m', ' ' * 5, '\033[1;31m♥\033[m')
print('\033[1;31m♦♣♠♥\033[m' * 6)

from random import choice
from time import sleep

lista = ['PEDRA', 'PAPEL', 'TESOURA']

def jokenpo():

    computador = choice(lista).upper() 

    print('\033[33mDigite Pedra, papel ou tesoura.\033[m')
    escolha = str(input()).strip().upper()

    if escolha in lista:
        print('\033[34mJO')
        sleep(1)
        print('\033[34mKEN')
        sleep(1)
        print('\033[34mPÔ!')

        sleep(1.5)

        if computador == escolha:
            print('\033[34mInfelizmente dessa vez não houve vencedor\033[m')
        elif {(computador == 'TESOURA' and escolha == 'PAPEL') or 
              (computador == 'PEDRA' and escolha == 'TESOURA') or 
              (computador == 'PAPEL' and escolha == 'PEDRA')}:
            print('\033[31mMUAHAHAHA! VENCI!!\033[m')
        else:
            print('\033[35mVocê teve sorte dessa vez...\033[m')

        sleep(1.5)
        
        print('\033[34mComputador  - {}\nPlayer - {}\033[m'.format(computador.capitalize(), escolha.capitalize()))

    else:
        print('\033[31mPor favor digite uma opção válida.\033[m\n')
        jokenpo()

jokenpo()

while True:
    escolha = input('\n\033[1;33mDeseja jogar novamente? [S/N]\033[m\n')
    if escolha.upper() == 'S' or escolha.upper() == 'SIM':
        jokenpo()
        print('\n')
    elif escolha.upper() == 'N' or escolha.upper() == 'NÃO':
        print("\033[33mObrigado por jogar!\033[m")
        break
    
    elif escolha in '':
        print('\033[1;31mOpção Inválida!\nDigite S para Sim ou N para Não.\nVocê não digitou nada.\033[m')

    else:
        print(f'\033[1;31mOpção Inválida!\nDigite S para Sim ou N para Não.\nVocê digitou {escolha}\033[m')

            