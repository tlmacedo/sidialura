class Conta:

	def __init__(self, numero, titular, saldo, limite):
		print('Construindo objeto... {}'.format(self))
		self.__numero = numero
		self.__titular = titular
		self.__saldo = saldo
		self.___limite = limite

	@property
	def numero(self):
		return self.__numero

	@property
	def titular(self):
		return self.__titular

	@property
	def saldo(self):
		return self.__saldo

	@property
	def limite(self):
		return self.__limite

	@limite.setter
	def limite(self, limite):
		self.__limite = limite

	def depositar(self, valor):
		self.__saldo += valor

	def sacar(self, valor):
		self.__saldo -= valor

	def extrato(self):
		print('Saldo de {} do titular: {}'.format(self.__saldo, self.__titular))

	def transferir(self, valor, conta_destino):
		self.sacar(valor)
		conta_destino.depositar(valor)
