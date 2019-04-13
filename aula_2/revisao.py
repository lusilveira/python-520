lista_de_gatos = [
	{
		'Nome': 'gato',
		'Peso': 5000,
		'Idade': 6,
		'Apelido': 'sedoso'
	},

	{
		'Nome': 'Fernado',
		'Peso': 3750,
		'Idade': 3,
		'Apelido': 'Brilhoso'
	}
]
'''
def get_input_as_int(mensagem):
	user_input = input(mensagem)
	for token in user_input:
		print('Caracter atual: {}'.format(token))
		if token not in '0123456789':
			print('Caracter invalido encontrado')
			print('Encerrado o algoritmo com erro')
			return -1
	print('Algoritmo executado com sucesso!')
	return int(user_input)

get_input_as_int('Caso de teste:\n')

	#solução nutela
	#if user_input.isdigit():
	#return int(user_input)
exit()
'''

def get_input_as_int(mensagem,erro):
	user_input = input(mensagem)
	try:
		return int(user_input)
	except ValueError:
		raise ValueError(erro)

def tratamento_de_tentativas(numero_tentativas,mensagem,erro):
	for tentativa in range(numero_tentativas):
		try: 
			return get_input_as_int(mensagem,erro)
		except ValueError as err:
			restantes = numero_tentativas - (tentativa + 1)
			print('Um erro aconteceu, Você ainda tem {} tentativas'.format(restantes))
			print(err)
	print('Você errou o input {} vezes.' .format(numero_tentativas))
	print('Vou encerrar o programa')
	exit()

'''
valor_retorno = tratamento_de_tentativas(
	3,					#numero de tentativas
	'Caso de teste:\n', #mensagem para o usuario
	'Deve ser um número !!!!! >.<' #erro
)		

print(valor_retorno)
exit()
'''

novo_gato = {
	'Nome': input ('Digite seu nome:\n'),
	'Peso': tratamento_de_tentativas (
		5, 'Digite o peso:\n','O peso deve ser um número maior que 0'
	),
	'Idade': tratamento_de_tentativas(
		3, 'Digite a idade:\n','A idade deve ser maior que 1cl'
	),
	'Apelido': input ('Digite o apelido:\n')
}
lista_de_gatos.append(novo_gato)


for gato in lista_de_gatos:
	print('Peso do gato: {}'.format(gato['Peso']))
	if gato ['Peso'] > 4000:
		print('Esse é o gato')
	else:
		print('Ela é a Malawi')

exit()

# teste de sanidade do interpretador
#print('hello,world')