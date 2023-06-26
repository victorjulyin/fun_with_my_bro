import time
from random import randint

for i in reversed(range(1,4)):
    time.sleep(1)
    print(i)

movies = {
    'Дарья Зубарева':      'Здравствуй, мир',
    'Нина Зубарева':       'Для каждой тебя, что я раньше любил',
    'Юлия Зубарева':       'Девушка,подающая надежды',
    'Михаил Варфоломеев':  'Страшная воля Богов',
    'Виталий Варфоломеев': 'Водная жизнь'
}

def choose_movie() -> str:
    winner=list(movies.keys())[randint(0,4)]
    return winner

winner = choose_movie()

print(f"""Поздравляем, {winner}!
Удачного просмотра фильма под названием: {movies[winner]}.""")



'''
История просмотров:
25.06.2023 - Девушка, подающая надежды
'''