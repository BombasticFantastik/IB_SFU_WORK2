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

        #print(P,Q,N,d,s,e)
        

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

        final_acsitext=[int(''.join(txt)) for txt in codded_text]

        #-------------------------------------------

        
        self.coded_text_for_alice=[txt for txt in final_acsitext]
        print(self.coded_text_for_alice)
        self.coded_text_for_alice=self.coded_text_for_alice[0]
        print(self.coded_text_for_alice)
        self.coded_text_for_alice=pow(self.coded_text_for_alice,self.s,self.N)
        print(self.coded_text_for_alice)

        
        #print("Кнопка слева нажата!")
        
        #[101114114114114114114114114114] 7004512948217794123544388233 9548663343258338948137807531
        #[101114114114114114114114114]    7004512948217794123544388233 9548663343258338948137807531

    def on_right_button_clicked(self):
        print('---')
        print(self.coded_text_for_alice)
        
        


        #result = [pow(txt,self.e,selrf.N) for txt in self.coded_text_for_alice ]
        print(self.coded_text_for_alice,self.e,self.N)
        print(pow(self.coded_text_for_alice,self.e,self.N))
        result=[pow(self.coded_text_for_alice,self.e,self.N)]
        print(f'result:{result},e:{self.e},N:{self.N},s:{self.s}')
        
        final_result=[ASCII2text(str(txt),3) for txt in result ]
        #print(final_result)
        self.alice_input.setText(str(final_result[0]))
        #print("Кнопка справа!")

        print('____________________')


        

