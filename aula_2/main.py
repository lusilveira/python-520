
import aleatorio as foo

def gerar_lista_usuarios(n):
	lista = []
	for i in range(n):
		u =  foo.gerar_usuario_aleatorio()
		lista.append(u)
	return lista

foo.ASCII_LETTERS
lista_de_usuarios = gerar_lista_usuarios(100)

print ('Arquivo main.py: {}'.format(__name__))