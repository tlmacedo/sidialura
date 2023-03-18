class Programa:
	def __init__(self, nome, ano):
		self._nome = nome
		self._ano = ano
		self._likes = 0

	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, nome):
		self._nome = nome.title()

	@property
	def ano(self):
		return self._ano

	@property
	def likes(self):
		return self._likes

	def dar_like(self):
		self._likes += 1


class Filme(Programa):
	def __init__(self, nome, ano, duracao):
		super().__init__(nome, ano)
		self._duracao = duracao

	@property
	def duracao(self):
		return self._duracao


class Serie(Programa):
	def __init__(self, nome, ano, temporadas):
		super().__init__(nome, ano)
		self._temporadas = temporadas

	@property
	def temporadas(self):
		return self._temporadas
