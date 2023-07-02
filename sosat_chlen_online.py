import time
from random import randint
import tkinter as tk
from PIL import Image, ImageTk

movies = {
    'Дарья Зубарева':      'Здравствуй, мир',
    'Нина Зубарева':       'Для каждой тебя, что я раньше любил',
    'Юлия Зубарева':       'Девушка,подающая надежды',
    'Михаил Варфоломеев':  'Страшная воля Богов',
    'Виталий Варфоломеев': 'Водная жизнь'
}

def choose_movie() -> str:
    winner = list(movies.keys())[randint(0, 4)]
    return winner


def show_winner():
    winner = choose_movie()
    message = f"Поздравляем, {winner}! Удачного просмотра фильма под названием: {movies[winner]}."
    output_label.config(text=message)

    # Загрузка файла с изображением
    image_path = f"{winner}.png" # Допустим, файл называется так же, как имя фильма + расширение .png
    image_path=r"C:\Users\varfo\OneDrive\Рабочий стол\hui"
    try:
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        photo_label = tk.Label(image=photo)
        photo_label.image = photo # Ссылка на изображение нужна, чтобы изображение не было случайно удалено сборщиком мусора
        photo_label.pack(pady=20) # Отображение изображения
    except FileNotFoundError:
        print(f"Файловое изображение {image_path} не найдено")
root = tk.Tk()
root.title("Выбор фильма")

label = tk.Label(root, text="Нажмите на кнопку, чтобы выбрать фильм", font=("Arial", 14))
label.pack(pady=20)

choose_button = tk.Button(root, text="Выбрать", width=10, height=2, command=show_winner)
choose_button.pack()

# создание виджета для вывода сообщения
output_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
output_label.pack(pady=20)

root.mainloop()