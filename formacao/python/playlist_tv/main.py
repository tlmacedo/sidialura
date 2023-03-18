from src.br.com.tlmacedo.playlist_tv.modelo import Filme, Serie

vingadores = Filme('Vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
# print(
# 	f'{vingadores.__class__.__name__}: {vingadores.nome} - Ano: {vingadores.ano} [{vingadores.duracao}] - Likes: {vingadores.likes}')

atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
# print(
# 	f'{atlanta.__class__.__name__}: {atlanta.nome} - Ano: {atlanta.ano} [{atlanta.temporadas}] - Likes: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]

print(f'Minha playlist:')
for programa in filmes_e_series:
	detalhes = f'{programa.duracao} min' if isinstance(programa, Filme) else f'{programa.temporadas} Temp'
	print(
		f'{programa.__class__.__name__}: {programa.nome} - Ano: {programa.ano} [{detalhes}] - Likes: {programa.likes}')
