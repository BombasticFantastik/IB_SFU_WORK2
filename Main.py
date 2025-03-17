from Big_math import find_NPQ,find_s,euclid_method
from Window import ImageViewer
from PyQt6.QtWidgets import QApplication
import sys

N,P,Q=find_NPQ()
d=(P-1)*(Q-1)
s=find_s(d)
e,y,x=euclid_method(d,s)
e=d-abs(min(x,y))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageViewer(P,Q,N,d,s,e)
    window.show()
    sys.exit(app.exec())