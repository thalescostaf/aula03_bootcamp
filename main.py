# O primeiro controle de fluxo é o IF
# É o mais comum

print('Primeiro exemplo')
x = -5
if x <= 2:
    print('É menor que zero')
elif x <= 0:
    print('É menor que dois')
else:
    print('É maior')


print('===== Exercio para ver se é negativo')

quantidade = -40
preco = -3

if quantidade > 0 and preco > 0:
    print('Valores validos')
else:
    print('Valores negativos')


print('===== Exemplo com FOR')

for i in range (1,5):
    print(i)



print('===== Exercio listas')

lista_de_alunos = ['Thales', 'Fabio', 'Luciano', 'Lais']

for aluno in lista_de_alunos:
    print(aluno)


