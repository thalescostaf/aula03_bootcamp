import time
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

print('===== Contando palavras em string com FOR')

texto = 'thales costa fernandes fernandes costa thales c f'

palavras = texto.split()
print(palavras)

contagem_de_palavras = {}

# Vamos percorrer todas as palavras dentro de palavra e checar se está na contagem

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] = +1
        pass
    else:
        contagem_de_palavras[palavra] = 1
        print(contagem_de_palavras)


print('===== Exercio WHILE')

#condicao = True

#while condicao:
#    print('Execute meu código')
#    time.sleep(5)



print('===== novo desafio')

nome_valido = False

while nome_valido is not True:
    try:
        nome = input('Digite seu nome: ')
        
        if len(nome) == 00:
            raise ValueError('O nome não pode estar vazio')
        elif any(char.isdigit() for char in nome):
            raise ValueError('O nome não pode conter numeros')
        else:
            nome_valido = True
            print('Nome Válido: ', nome)
    except ValueError as e:
            print(e)