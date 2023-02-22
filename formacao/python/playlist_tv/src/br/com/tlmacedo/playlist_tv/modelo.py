class Filme:
	def __init__(self, nome, ano, duracao):
		print('criando {}...'.format(self.__class__.__name__))
		self.__nome = nome
		self.__ano = ano
		self.__duracao = duracao
		self.__likes = 0

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, nome):
		self.__nome = nome.title()

	@property
	def ano(self):
		return self.__ano

	@property
	def duracao(self):
		return self.__duracao

	@property
	def likes(self):
		return self.__likes

	def dar_like(self):
		self.__likes += 1


class Serie:
	def __init__(self, nome, ano, temporadas):
		print('criando {}...'.format(self.__class__.__name__))
		self.__nome = nome.title()
		self.__ano = ano
		self.__temporadas = temporadas
		self.__likes = 0

	@property
	def nome(self):
		return self.__nome

	@property
	def ano(self):
		return self.__ano

	@property
	def temporadas(self):
		return self.__temporadas

	@property
	def likes(self):
		return self.__likes

	def dar_likes(self):
		self.__likes += 1
