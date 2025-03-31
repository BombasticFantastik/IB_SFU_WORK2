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

        self.setWindowTitle("Интерфейс с фотографиями и кнопками")
        self.setGeometry(100, 100, 100, 100)

        self.bob_input=QLineEdit()
        self.alice_input=QLineEdit()

        self.bob_your_text_label=QLabel("Введите текст Боба")
        self.alice_your_text_label=QLabel("Сообщение Алисы")
        

        self.button_left = QPushButton("Кнопка слева", self)
        self.button_right = QPushButton("Кнопка справа", self)

        self.button_left.clicked.connect(self.on_left_button_clicked)
        self.button_right.clicked.connect(self.on_right_button_clicked)


        # Создание layout'ов
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.bob_your_text_label)
        left_layout.addWidget(self.bob_input)
        left_layout.addWidget(self.button_left)
        

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.alice_your_text_label)
        right_layout.addWidget(self.alice_input)
        right_layout.addWidget(self.button_right)



        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)

    

    def on_left_button_clicked(self):
        text=split_text(self.bob_input.text())
        #print(text2ASCII(text[0]))
        codded_text=[text2ASCII(txt)[0] for txt in text]#получается лист закодированных слов 
        steps=[text2ASCII(txt)[1] for txt in text]#получается лист шагов
        print(codded_text)
        print(steps)
        






        #text_for_return=''.join(codded_text)
        # text=[part for part in split_text(self.bob_input.text())]
        # acsitext,self.step=[text2ASCII(part) for part in text ]
        # merge_acsitext=[''.join(part) for part in acsitext]
        # final_acsitext=''.join(merge_acsitext)








        final_acsitext=int(''.join(codded_text[0]))#временно 0
        print(final_acsitext)
        
        
        
        self.alice_input.setText(str(pow(final_acsitext,self.s,self.N)))
        print("Кнопка слева нажата!")

    def on_right_button_clicked(self):
        print(int(self.alice_input.text()))
        result = pow(int(self.alice_input.text()),self.e,self.N)
        print(result)
        final_result=ASCII2text(str(result),3)
        self.alice_input.setText(str(final_result))
        print("Кнопка справа!")


        

