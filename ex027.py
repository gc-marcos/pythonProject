nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Seja bem vindo(a) {}'.format(n[0]))
print('Primeiro nome é {}.'.format(n[0]))
print('Últino nome é {}.'.format(n[len(n)-1]))
