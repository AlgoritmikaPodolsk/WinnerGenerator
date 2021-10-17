#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint


app = QApplication([])
#создание элементов интерфейса
#главное окно
main_win = QWidget()
main_win.resize(400, 200)
main_win.setWindowTitle('Определитель победителя')

#виджеты окна - кнопка и надписи
button = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')

#привязка элементов к вертикальной линии
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)

#обработка событий
def show_winner():
    '''функция, которая генерирует и показывает число'''
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Победитель:')

button.clicked.connect(show_winner)

#запуск приложения
main_win.show()
app.exec_()