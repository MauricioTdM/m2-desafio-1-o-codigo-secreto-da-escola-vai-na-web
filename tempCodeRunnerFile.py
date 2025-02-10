def contar_letras(palavra):
    quantidade = len(palavra)
    return quantidade

nome = input('Digite um nome: ')
quantidade_letras = contar_letras(nome)

print(f'O nome {nome} tem {quantidade_letras} letras')