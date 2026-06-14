''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Sao Paulo',
          'Athletico-PR', 'Red Bull Bragantino', 'Bahia', 'Coritiba',
          'Cruzeiro', 'Botafogo', 'Vitoria', 'Atletico-MG',
          'Internacional', 'Gremio', 'Corinthias', 'Vasco da Gama',
          'Santos', 'Mirassol', 'Remo', 'Chapecoense')
print('-=' * 15)
print('Lista de times do Brasileirão: ', end='')
print(times)
print('-=' * 15)

print('Os 5 primeiros são: ', end='')
print(times[0:5])
print('-=' * 15)

print('Os ultimos 4 colocados: ', end='')
print(times[-4:])
print('-=' * 15)

print('Times em ordem alfabetica: ', end='')
print(sorted(times))
print('-=' * 15)

print(f'A Chapecoense está na {times.index('Chapecoense')+1} posição')