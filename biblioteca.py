+# -*- coding: latin1 -*-
 +
 +class Usuario:
 +	def __init__(self):
 +		self.logins[]
 +		self.senhas[]
 +#Classe Básica! Apenas armazenando 2 listas. Logins e Senhas :) (Acho que isso aqui vai dar erro como ta)
 +
 +"""
 +Há um erro infernal na classe de baixo (Cadastrar)
 +Ela fica pedindo a existencia de "LOGINS" o tempo todo. Mas não sei como adicionar isso, e LOGINS só deveria
 +ser uma variavel da classe USUARIO (classe pai)
 +"""
 +class Cadastrar(Usuario):
 +	def cnome(self):
 +		self.erro=0
 +		while self.erro==0:
 +			print "Digite seu nome:"
 +			self.cadnome = raw_input()
 +			print "ERRO?", self.cadnome
 +			if len(self.cadnome) <= 2:
 +				print "Seu nome deve ter 3 ou mais caracteres"
 +				self.erro=0
 +
 +
 +	def csenha(self):
 +		while self.erro==0:
 +
 +			print "Digite sua senha:"
 +			self.cadsenha = raw_input()
 +
 +			if len(self.cadsenha) <4:
 +				print "Senha muito pequena, deve ter no minimo 4 caracteres"
 +				self.erro=0
 +
 +
 +class Menu:
 +	def __init__(self):
 +		print "Bem-Vindo:"
 +		print "1 - Login"
 +		print "2 - Cadastro"
 +		self.men=int(raw_input())
 +
 +		"""
 +		ESSA classe serve para fazer o MENU!
 +		Veja que os prints mostram o que o usario deve fazer.
 +		As classes abaixo são para o login e o cadastro.
 +		"""
 +
 +class Cad(Menu):
 +	def __init__(self):
 +		Cadastrar().cnome()
 +		Cadastrar().csenha()
 +		Usuario()
 +		Usuario().logins.append(Cadastrar().cadnome)
 +		Usuario().senhas.append(Cadastrar().cadsenha)
 +		"""
 +		Def simples, ele vai chamar as funções cadastrar nome (cnome) e cadastrar senha (csenha)
 +		caso as funções terminem (significa que as 2 foram OKAY!) ele vai chamar Usuario e adicionar
 +		o cad nome em LOGINS e o cadsenha em SENHAS. Tudo armazenado nessa lista, temos um novo usuario :D
 +		"""
 +
 +
 +
 +class Login(Menu):
 +	def __init__(self):
 +		print "Digite seu nome:"
 +		nome=raw_input()
 +			
 +		print "Digite sua senha:"
 +		senha=raw_input()
 +			
 +		Usuario()
 +		if nome in self.logins:
 +			self.posicao = self.logins.index
 +			if senha == self.senhas[self.posicao]:
 +				print "Acesso Permitido"
 +			else:
 +				print "Acesso Negado! Senha Invalida!"
 +
 +		else:
 +			print"Usuario nao cadastrado" 
 +			
 +			"""
 +			O que diabos essa def faz? Simples! Pede para que o 
 +			usuario digite seu login e senha, apois isso ele procura LOGIN na lista dos LOGINS já existentes (VEJA que chamam a classe USUARIO)
 +			caso existe ele procura ver se a senha é a mesma.
 +			"""
 +
 +
 +menu=Menu()
 +if menu.men == 1:
 +	Login()
 +if menu.men == 2:
 +	Cad()

