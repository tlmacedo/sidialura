class Conta:

	def __init__(self, numero, titular, saldo, limite):
		print('Construindo objeto... {}'.format(self))
		self.__numero = numero
		self.__titular = titular
		self.__saldo = saldo
		self.__limite = limite

	@staticmethod
	def codigo_banco():
		return "001"

	@staticmethod
	def codigos_bancos():
		return {"BB": "001", "Caixa": "104", "Bradesco": "237"}

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
		if self.__pode_sacar(valor):
			self.__saldo -= valor
		else:
			print("O valor {} passou o limite".format(valor))

	def extrato(self):
		print('Saldo de {} do titular: {}'.format(self.__saldo, self.__titular))

	def transferir(self, valor, conta_destino):
		self.sacar(valor)
		conta_destino.depositar(valor)

	def __pode_sacar(self, valor_a_sacar):
		saldo_disponivel = self.__saldo + self.__limite
		return valor_a_sacar <= saldo_disponivel
