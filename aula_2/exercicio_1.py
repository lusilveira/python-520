# Missão 1:
# Criar uma função 'cadastrar_usuario'
# que retorne um dicionário de usuário.
# O dicionário deve conter a propriedades:
# - nome
# - email
# - idade
# e os valores devem ser digitados 
# pelo usuário do através do terminal (input)


def cadastrar_usuario ():
	novo_usuario =  {
		'Nome': input ('Digite seu nome:\n'),
		'Email': input ('Digite seu Email:\n'),
		'Idade': input ('Digite seu Idade:\n'),
	}
	return novo_usuario

novo_usuario = cadastrar_usuario()
#{'nome': Luciana, 'email': lu@gmail.com, 'idade': 37}
print(novo_usuario)

