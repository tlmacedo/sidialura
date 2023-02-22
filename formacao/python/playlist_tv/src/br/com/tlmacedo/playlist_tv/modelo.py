class Filme:
	def __init__(self, nome, ano, duracao):
		print('criando {}...'.format(self.__class__.__name__))
		self.__nome = nome
		self.__ano = ano
		self.__duracao = duracao

	@property
	def nome(self):
		return self.__nome


class Serie:
	def __init__(self, nome, ano, temporadas):
		print('criando {}...'.format(self.__class__.__name__))
		self.__nome = nome
		self.__ano = ano
		self.__temporadas = temporadas

	@property
	def nome(self):
		return self.__nome

	@property
	def ano(self):
		return self.__ano

	@property
	def temporadas(self):
		return self.__temporadas
