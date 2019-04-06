usuario = {
	'nome': input('Digite seu nome: '),
	'idade': input('Digite sua idade: '),
	'email': input('Digite seu email: ')
}
nome = usuario['nome']
print('usuario {} cadastrado com sucesso !' .format(nome))

exit()
lista_populada = [1,2,3,4,5,6,7,8,9,10]
lista_vazia = []

#Para inserir elementos em uma lista
lista_vazia.append(1)
lista_vazia.append(2)
lista_vazia.append(3)
lista_vazia.append(4)
lista_vazia.append(5)
lista_vazia.append(6)
lista_vazia.append(7)
lista_vazia.append(8)
lista_vazia.append(9)
lista_vazia.append(10)
print(lista_populada)
print(lista_vazia)

#Primeiro Elemento
print(lista_vazia[0])
# Imprimir apenas o quinto elemento da lista_vazia
print(lista_vazia[4])

for n in lista_vazia:
	print('Imprimindo o número  ' + str(n))
	print('FIM DO LOOP')

