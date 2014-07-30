# -*- coding: latin1 -*-
import os
import pydoc
class Usuario:
	logins=[]
	senhas=[]
	jogo= []
#Classe Básica! Apenas armazenando 3 listas. Logins e Senhas e armazenara os jogos :)


class Armazenar:
	armazena=0
	lj=[]

"""
A classe cadastrar agora funcionar.
Esta definida em 2 defs para que cada um faça apenas um cadastro, ficando mais fácil lá em baixo a organização
"""
class Cadastrar(Usuario):
	"""
    Aqui temos o processo de criação do usuário
    e senha respectivamente.
    """	

	def cnome(self):
		"""
		Usuario deverá ser inserido aqui,
		acontecerá uma verificação
		para não ocorrerem
		usuários iguais.
		"""
		self.erro=0
		while self.erro==0:
			print "Digite seu nome:"
			self.cadnome = raw_input()
			os.system("cls")
			if len(self.cadnome) <= 2:
				print "Seu nome deve ter 3 ou mais caracteres"
				self.erro=0
			elif self.cadnome in Usuario().logins:
				print "Nome Ja existente"
				self.erro=0
			else:
				self.erro=1
		return self.cadnome
		os.system("cls")


	def csenha(self):
		""" 
		Aqui é onde entra a senha.
		terá de ter ao menos 4 caracteres e será
		armazenada em uma lista.
		"""
		self.erro=0
		while self.erro==0:

			print "Digite sua senha:"
			self.cadsenha = raw_input()
			os.system("cls")

			if len(self.cadsenha) <4:
				print "Senha muito pequena, deve ter no minimo 4 caracteres"
				self.erro=0
			else:
				self.erro=1
		return self.cadsenha
		os.system("cls")

class Menu:
	def m1(self):
		"""
		Primeiro menu do programa. 
		Aqui o usuario vai inserir a opção desejada.
		"""
		print "Bem-Vindo:"
		print "1 - Login"
		print "2 - Cadastro"
		print "3 - Sair"
		self.men=int(raw_input())
		os.system("cls")

		"""
		ESSA classe serve para fazer o MENU!
		Veja que os prints mostram o que o usario deve fazer.
		As classes abaixo são para o login e o cadastro.
		"""
	def m2(self):
		"""
		Segundo menu principal do aplicativo.
		Aqui é a tela de logon do usuário,
		onde encontram-se todas as opções de 
		interação com o programa (enquanto logado)
		"""
		print "1 - Cadastrar Jogo"
		print "2 - Listar Jogos"
		print "3 - Deletar Jogo"
		print "4 - Editar Usuario"
		print "5 - Deslogar"
		self.men=int(raw_input())
		os.system("cls")

class Cad(Menu, Usuario):
	def __init__(self):
		self.nn=Cadastrar().cnome()
		self.ns=Cadastrar().csenha()
		Usuario()
		Usuario().logins.append(self.nn)
		Usuario().senhas.append(self.ns)
		self.jogador=[]
		Usuario().jogo.append(self.jogador)
		"""
		Def simples, ele vai chamar as funções cadastrar nome (cnome) e cadastrar senha (csenha)
		caso as funções terminem (significa que as 2 foram OKAY!) ele vai chamar Usuario e adicionar
		o cad nome em LOGINS e o cadsenha em SENHAS. Tudo armazenado nessa lista, temos um novo usuario :D
		A variavel com nome de self.jogador serve para adicionar uma lista dentro da lista jogador, isso será
		útil para cadastrar os jogos
		"""

class Login(Menu):
	"""
	Aqui acontecem as operações de login.
	Inserir o usuario e a senha na tela.
	"""
	def __init__(self):
		nome = ""
		senha= ""

	def loga(self):
		print "Digite seu nome:"
		nome=raw_input()
			
		print "Digite sua senha:"
		senha=raw_input()
			
		Usuario()
		if nome in Usuario().logins:
			self.posicao = Usuario().logins.index(nome)
			if senha == Usuario().senhas[self.posicao]:
				print "Acesso Permitido"
				return Usuario().logins.index(nome)
			else:
				print "Acesso Negado! Senha Invalida!"
				return 9999
		else:
			print"Usuario nao cadastrado"
			return 9999

"""
O que diabos essa def faz? Simples! Pede para que o 
usuario digite seu login e senha, apois isso ele procura LOGIN na lista dos LOGINS já existentes (VEJA que chamam a classe USUARIO)
caso existe ele procura ver se a senha é a mesma.
"""

class Jogos:
	def __init__(self):
		self.jogo1={"Nome":"Doom", "Desenvolvedora":"Id Software","Lancamento":"10 de dezembro de 1993"}
		self.jogo2={"Nome":"Zombies Ate My Neighbors", "Desenvolvedora":"LucasArts","Lancamento":"19 de Julho de 1994" }
		self.jogo3={"Nome":"Fallout", "Desenvolvedora":"Black Isle Studios","Lancamento":"15 de Novembro de 1997" }
		self.jogo4={"Nome":"Spider-Man", "Desenvolvedora":"Neversoft","Lancamento":"24 de Agosto de 2000" }

"""Classe feita apenas para criar os dicionarios! Cada dicionario representa um jogo será útil na hora do cadastro dos jogos na conta do usuario"""

class Cajogo:
	"""
	Aqui os jogos serão cadastrados,
	separados por números (não vetores)
	selecionados pelo usuario.
	"""
	def __init__(self):
		print "Qual jogo deseja cadastrar?"
		self.provisorio=[]
		Jogos()
		print "   ", Jogos().jogo1.keys()
		print "1 -",Jogos().jogo1.values()
		print "2 -",Jogos().jogo2.values()
		print "3 -",Jogos().jogo3.values()
		print "4 -",Jogos().jogo4.values()
		cadjogo = int(raw_input())
		Usuario()
		Armazenar()
		if Armazenar().lj:
			Armazenar().lj.pop
		self.ponto=Armazenar().armazena
		if cadjogo == 1:
			self.provisorio=Usuario().jogo[self.ponto]
			self.provisorio.append(Jogos().jogo1.values())
			Usuario().jogo[self.ponto]=self.provisorio
			Armazenar().lj.append(Jogos().jogo1.values())
		if cadjogo == 2:
			self.provisorio=Usuario().jogo[self.ponto]
			self.provisorio.append(Jogos().jogo2.values())
			Usuario().jogo[self.ponto]=self.provisorio
			Armazenar().lj.append(Jogos().jogo2.values())
		if cadjogo == 3:
			self.provisorio=Usuario().jogo[self.ponto]
			self.provisorio.append(Jogos().jogo3.values())
			Usuario().jogo[self.ponto]=self.provisorio
			Armazenar().lj.append(Jogos().jogo3.values())
		if cadjogo == 4:
			self.provisorio=Usuario().jogo[self.ponto]
			self.provisorio.append(Jogos().jogo4.values())
			Usuario().jogo[self.ponto]=self.provisorio
			Armazenar().lj.append(Jogos().jogo4.values())

"""
Classe de cadastro, Esse Armazenar().lj no final ainda é uma gambiarra que não funciona, preciso dela para poder fazer algumas anotações
para mais tarde poder usar a classe deletar. Tentar ver qual o erro!
"""

class Listar:
	"""
	Listar os jogos do usuário.
	"""
	def __init__(self):
		Usuario()
		Armazenar()
		self.ponto=Armazenar().armazena
		print Usuario().jogo[self.ponto]

class Deletar:
	"""
	Deleta os jogos que o usuário deseja.
	"""
	def __init__(self):
		Usuario()
		Armazenar()
		self.ponto=Armazenar().armazena
		Listar()
		print "Qual o numero do jogo que voce deseja deletar?"
		ndel=int(raw_input())
		"""
		if ndel in Armazenar().lj:
			self.posi=Armazenar().lj.index(ndel)
			Armazenar().lj.pop(self.posi)
			Usuario().jogo[self.ponto]=Armazenar().lj
		else:
			print "PUTA QUE PARIU!!!!"
		"""
		if Armazenar().lj[ndel]:
			Armazenar().lj.pop(ndel)
			Usuario().jogo[self.ponto]=Armazenar.lj

class Atualizar:
	"""
	Aqui o usuário pode fazer alterações
	no seu nick e senha. Coisa simples.
	"""
	def __init__(self):
		Usuario()
		Armazenar()
		self.ponto=Armazenar().armazena
		print "Deseja alterar Nome ou Senha?"
		alt = raw_input()

		if alt == "nome":
			print "Digite seu novo nome"
			nonome = raw_input()
			Usuario().logins[self.ponto]=nonome

		if alt == "senha":
			print "Digite sua nova senha"
			nose = raw_input()
			Usuario().senhas[self.ponto]=nose


erro=9999
sair=1
while sair != 0:
	while erro == 9999 and sair != 0:
		menu=Menu()
		menu.m1()
		if menu.men == 1:
			erro=Login().loga()
			Armazenar().armazena=erro
		if menu.men == 2:
			Cad()
		if menu.men == 3:
			sair = 0

	if erro != 9999:

		while erro!=9999:
			print "Bem-Vindo Usuario: ", Usuario().logins[erro]
			menu=Menu()
			menu.m2()
			if menu.men == 1:
				Cajogo()
			if menu.men == 2:
				Listar()
			if menu.men == 3:
				Deletar()
			if menu.men == 4:
				Atualizar()
			if menu.men == 5:
				erro=9999

a=raw_input()
