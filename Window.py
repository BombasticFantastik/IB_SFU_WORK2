import sys
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QLineEdit
from PyQt6.QtGui import QPixmap
from Text_spliter import text2ASCII,split_text,ASCII2text

class ImageViewer(QWidget):
    def __init__(self,P,Q,N,d,s,e):
        super().__init__()
        self.P=P
        self.Q=Q
        self.N=N
        self.d=d
        self.s=s
        self.e=e

        # Настройка окна
        self.setWindowTitle("Интерфейс с фотографиями и кнопками")
        self.setGeometry(100, 100, 100, 100)

        # Загрузка изображений
        self.image_left = QPixmap("bob.jpg")  # Укажите путь к левому изображению
        self.image_right = QPixmap("alice.jpg")  # Укажите путь к правому изображению

        # Создание меток для изображений
        self.label_left = QLabel(self)
        self.label_left.setPixmap(self.image_left)
        self.label_left.setScaledContents(True)

        self.label_right = QLabel(self)
        self.label_right.setPixmap(self.image_right)
        self.label_right.setScaledContents(True)

        #создание инпутов
        self.bob_input=QLineEdit()
        self.alice_input=QLineEdit()

        #создание лейблов
        self.bob_your_text_label=QLabel("Введите текст Боба")
        self.center_label=QLabel("Зашифрованное сообщение")

        #создание кнопок
        self.button_left = QPushButton("Кнопка слева", self)
        self.button_right = QPushButton("Кнопка справа", self)

        # Подключение кнопок к функциям
        self.button_left.clicked.connect(self.on_left_button_clicked)
        self.button_right.clicked.connect(self.on_right_button_clicked)

        # Создание layout'ов
        left_layout = QVBoxLayout()
        #left_layout.addWidget(self.label_left)
        left_layout.addWidget(self.bob_your_text_label)
        left_layout.addWidget(self.bob_input)
        left_layout.addWidget(self.button_left)
        

        right_layout = QVBoxLayout()
        #right_layout.addWidget(self.label_right)
        right_layout.addWidget(self.alice_input)
        right_layout.addWidget(self.button_right)

        center_layout = QVBoxLayout()
        center_layout.addWidget(self.center_label)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(center_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

    def on_left_button_clicked(self):
        text=[part for part in split_text(self.bob_input.text())]
        acsitext,self.step=[text2ASCII(part) for part in text ]
        
       
        merge_acsitext=[''.join(part) for part in acsitext]
        
        final_acsitext=''.join(merge_acsitext)
        final_acsitext=int(final_acsitext)

        result=pow(final_acsitext,self.s,self.N)


        self.center_label.setText(str(result))
        print("Кнопка слева нажата!")

    def on_right_button_clicked(self):
        text=int(self.center_label.text())
        result=pow(text,self.s,self.N)

        text_result=ASCII2text(result,self.step)
        
        self.alice_input.setText(str(text_result))


        

