# Ex 60 Ler um número e mostrar seu fatorial 

num = int(input('Digite um valor: '))
fatorial = 1
while num > 1:
    fatorial *= num
    num = num - 1


print(fatorial)

'''fac = 1
for numero in range(num, 0, - 1):
    fac *= numero

print(fac)
'''

# Método Guanabara

num = int(input('Digite um valor: '))
contagem = num
f = 1
print(f'Calculando {num}! = ', end='')
while contagem > 0:
    print(f'{contagem}', end='')
    print(' x ' if  contagem > 1 else ' = ', end='')
    f *= contagem
    contagem -= 1
print(f)