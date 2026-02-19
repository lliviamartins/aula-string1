nome=input('qual é o seu nome?')
print ('Olá',nome,'seja bem vindo(a)')
senha=input('digite sua senha')
print(senha)
dominio=input('digite o seu dominio')
print (dominio)
email=nome+'@'+dominio
print ('O seu e-mail é:',email)

palavra = 'jaca'
#colocar a string como toda maiuscula
print('Colocando o texto em maisculo: ', palavra.upper())
      
PALAVRA= 'JACA'
#colocar a string como toda minusculo
print('Colocando o texto em minusculo: ', PALAVRA.lower())
#contar caracter da string
palavra_contar = 'banana'
print('contar a letra b', palavra_contar.count('b'))
print('contar a letra a', palavra_contar.count('a'))
print('contar a letra n', palavra_contar.count('n'))
print('contar a letra a', palavra_contar.count('a'))
print('contar a letra n', palavra_contar.count('n'))
print('contar a letra a', palavra_contar.count('a'))

email2= email
letraA= email2.count ('a')
letraE= email2.count ('e')
letraI= email2.count ('i')
letraO= email2.count ('o')
letraU= email2.count ('u')


senha = 'a'+str(letraA) +'e'+str( letraE) +'i'+str( letraI) +'o'+str( letraO)+ 'u'+ str(letraU)
print("A sua senha é:", senha)


nome2=nome.lower()
letraA= nome2.count ('a')
letraE= nome2.count ('e')
letraI= nome2.count ('i')
letraO= nome2.count ('o')
letraU= nome2.count ('u')

usuario=nome+str(letraA)+str(letraE)+str(letraI)+str(letraO)+str(letraU)
print(usuario)








