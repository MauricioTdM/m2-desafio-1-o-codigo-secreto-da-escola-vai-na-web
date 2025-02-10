# Missão 1: Restaurando as Regras Escolares

def verificar_aprovação(nota):
    if nota >= 5:
        print('O aluno foi aprovado!')
    else:
        print('Infelizmente o aluno foi reprovado...')

nota_aluno = float(input('Insira a nota do aluno: '))
verificar_aprovação(nota_aluno)

# -----------------------------------------------------

# Missão 2: O Sistema Eleitoral Secreto

def verificar_elegibilidade(idade):
    if idade >= 16:
        print('Parabéns, você pode votar!')
    else:
        print('Sinto muito, você ainda não pode votar. Somente quando fizer 16 anos.')

idade_usuario = int(input('Qual a sua idade? '))
verificar_elegibilidade(idade_usuario)

# -----------------------------------------------------

# Missão 3: Recuperando o Sistema de Notas

def classificar_nota_aluno(nota):
    if nota >= 90:
        print('Parabéns, você tirou A!')
    elif (nota >= 80) and (nota <= 89):
        print('Muito bem, você tirou B.')
    elif (nota >= 70) and (nota <= 79):
        print('Bom trabalho, você tirou C.')
    elif (nota >= 60) and (nota <= 69):
        print('Fique atento, você tirou D.')
    else:
        print('Estude um pouco mais, você tirou F.')

nota_aluno = float(input('Insira a nota do aluno: '))
classificar_nota_aluno(nota_aluno)

# -----------------------------------------------------

# Missão 4: Restaurando a Identificação de Números

def somar_numeros(num1, num2):
    return num1 + num2

primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número: '))

soma = somar_numeros(primeiro_numero, segundo_numero)
print(f'A soma entre {primeiro_numero} e {segundo_numero} é: {soma}')

# -----------------------------------------------------

# Missão 5: Recuperando o Cofre de Segurança

def verificar_senha(senha):
    if senha == 'Python123':
        print('A senha está correta!')
    else:
        print('Senha incorreta, tente novamente!')

senha_usuario = input('Informe a senha: ')
verificar_senha(senha_usuario)

# -----------------------------------------------------

# Missão 6: Reforçando a Segurança e a Contagem do Sistema

contador = 1

while contador <= 10:
    print(contador)
    contador += 1

# -----------------------------------------------------

# Missão 7: Organizando a Lista

lista_numeros = [8, 3, 10, 1, 5]
lista_ordenada = sorted(lista_numeros)
print(lista_ordenada)

# -----------------------------------------------------

# Missão 8: Acessando os Registros de Alunos

nome_alunos = ('Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo')
print(f'Primeiro nome da tupla: {nome_alunos[0]}')
print(f'Último nome da tupla: {nome_alunos[-1]}')

# -----------------------------------------------------

# Missão 9: Calculando Dobro de um Número

def dobro(numero):
    numero *= 2
    return numero

numero_inserido = float(input('Digite um número para calcular o dobro: '))
numero_dobrado = dobro(numero_inserido)

print(f'O dobro de {numero_inserido} é {numero_dobrado}')

# -----------------------------------------------------

# Missão 10: Contando Letras

def contar_letras(palavra):
    quantidade = len(palavra)
    return quantidade

nome = input('Digite um nome: ')
quantidade_letras = contar_letras(nome)

print(f'O nome {nome} tem {quantidade_letras} letras')
