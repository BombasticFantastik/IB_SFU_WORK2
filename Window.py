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
        codded_text=[text2ASCII(txt)[0] for txt in text]
        self.steps=[text2ASCII(txt)[1] for txt in text]
        
        final_acsitext=[int(''.join(txt)) for txt in codded_text]
        self.coded_text_for_alice=[pow(txt,self.s,self.N) for txt in final_acsitext]

    def on_right_button_clicked(self):

        result=[pow(txt,self.e,self.N) for txt in self.coded_text_for_alice ]
   
        final_result=[ASCII2text(str(result[i]),self.steps[i]) for i in range(len(result)) ]
        finaliche_text=[''.join(txt) for txt in final_result]     
        self.alice_input.setText(''.join(finaliche_text))
        




        

