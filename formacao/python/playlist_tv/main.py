from src.br.com.tlmacedo.playlist_tv.modelo import Filme, Serie

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'Filme: {vingadores.nome} - Ano: {vingadores.ano} [{vingadores.duracao}] - Likes: {vingadores.likes}')

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
print(f'Serie: {atlanta.nome} - Ano: {atlanta.ano} [{atlanta.temporadas}] - Likes: {atlanta.likes}')
