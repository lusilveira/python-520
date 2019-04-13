import random
import string

ASCII_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def gerar_nome_aleatorio():
	string = ''
	for n in range(random.randint(5,15)):
		string += random.choice(ASCII_LETTERS)
	return string

	'''return ''.join (
		random.choices (
			string.ascii_letters,
			k=random.randint(5, 15)
	) '''	
#for i in range(10):
#print(gerar_usuario_aleatorio())

def gerar_email_aleatorio():
	return gerar_email_aleatorio() + '@4linux'

def gerar_idade_aleatorio():
		return random.randint(24 , 55)	


def gerar_usuario_aleatorio():
	novo_usuario = {
		'Nome': gerar_nome_aleatorio(),
		'Email': gerar_email_aleatorio(),
		'Idade': gerar_idade_aleatorio()
	}
	return novo_usuario

if __name__ == '__main__':
	print('Rode seus teste sem erro de eles atrapalharem')
	print('Arquivo aleatorio.py: {}'.format(__name__))