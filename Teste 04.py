print('Obtendo informações de algo digitado')
print('')
something = input('Digite alguma coisa para ser analisada: ')
print('O tipo primitivo do que foi digitado é ', type(something))
print('Somente espaços? ', something.isspace())
print('É um número? ', something.isnumeric())
print('É alfabético? ', something.isalpha())
print('É alfanúmerico? ', something.isalnum())
print('Todo escrito em maiúsculo? ', something.isupper())
print('Todo escrito em minúsculo? ', something.islower())
print('Texto capitalizado? ', something.istitle())