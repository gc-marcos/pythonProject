digite = input('Digite qualquer coisa! ')
print('Este tipo é {}'.format(type(digite)))
print('Tem espaço? {}'.format(digite.isspace()))
print('Tem numero? {}'.format(digite.isnumeric()))
print('Tem letras? {}'.format(digite.isalpha()))
print('É alfanumerico? {}'.format(digite.isalnum()))
print('É maiuscula? {}'.format(digite.isupper()))
print('É minuscula? {} '.format(digite.islower()))
print('É capitalizado? {}'.format(digite.istitle()))
