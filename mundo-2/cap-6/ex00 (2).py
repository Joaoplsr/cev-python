# Ex 57 Ler o sexo de uma pessoa, porém só aceita o valor M ou F

print('----Bem Vindo----')
sexo = ''
while sexo == '':
    sexo = str(input('Digite seu gênero [M/F]:')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        sexo = ''
        print('Tente outra vez!')
print(f'Gênero {sexo} registrado com sucesso!')

# Método Guanabara

print('----Bem Vindo----')
sexo = str(input('Digite seu gênero [M/F]:')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input(f'Gênero {sexo} não é válido, tente novamente [M/F]:')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
    