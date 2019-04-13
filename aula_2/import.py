import os
import subprocess
import datetime
import time
import random

def cadastrar_usuario ():
	novo_usuario =  {
		'Data_Cadastro': datetime.datetime.now(),
		'Nome': input ('Digite seu nome:\n'),
		'Email': input ('Digite seu Email:\n'),
		'Idade': input ('Digite seu Idade:\n'),
	}
	return novo_usuario

#novo_usuario = cadastrar_usuario()
probabilidade = random.random()
if probabilidade < 0.5:
	cadastrar_usuario()
else:
	print('Opa,não deu sorte ....')
exit()
#print(novo_usuario)

#os.system('clear')
subprocess.run(['clear' ])

#time.sleep(10.0)
start_time = time.clock()
time.sleep(10.0)
print('Tempo gasto = {}'.format(time.clock() - start_time))

d = novo_usuario['Data_Cadastro']
print(d.strftime('São Paulo, %d de %B de %Y'))



#{'nome': Luciana, 'email': lu@gmail.com, 'idade': 37}