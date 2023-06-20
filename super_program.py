import time
from random import randint

for i in reversed(range(1,4)):
    time.sleep(0.2)
    print(i)

movies = {
    'Дарья Зубарева': 'Здравствуй, мир',
    'Нина Зубарева': 'film_name',
    'Юлия Зубарева': 'Девушка,подающая надежду',
    'Михаил Варфоломеев': 'Волк с Уолл Стрит',
    'Виталий Варфоломеев': 'Невидимый страж'
}

def choose_movie():
    winner=list(movies.keys())[randint(0,4)]
    if winner == 'Нина Зубарева':
        print(f'''К сожалению, победитель ({winner}) не выбрал фильм.
Функция выбора фильма будет запущена заново.''')
        winner = choose_movie()
    return winner

winner = choose_movie()

print(f"""Поздравляем, {winner}!
Удачного просмотра фильма под названием: {movies[winner]}.""")
