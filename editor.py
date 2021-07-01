import sys
import os
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

from PyQt5.QtWidgets import QAction,qApp,QMainWindow


class Notepad(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):

        self.text_area = QTextEdit()
        self.clear = QPushButton("Clear")
        self.open = QPushButton("Open")
        self.save = QPushButton("Save")

        v_box = QVBoxLayout()

        v_box.addWidget(self.text_area)
        h_box = QHBoxLayout()

        h_box.addWidget(self.open)
        h_box.addWidget(self.save)

        v_box.addLayout(h_box)
        self.setLayout(v_box)

 
        self.open.clicked.connect(self.open_doc)
        self.save.clicked.connect(self.save_doc)

        self.setWindowTitle("NotePad")
        self.setWindowIcon(QIcon('/media/icon.svg'))
        self.show()
    



    def open_doc(self):
        doc_name = QFileDialog.getOpenFileName(self,"Open Doc",os.getenv("HOME"))

        with open(doc_name[0],"r") as file:
            self.text_area.setText(file.read()) 

    def save_doc(self):
        doc_name = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))

        with open(doc_name[0],"w") as file:

            file.write(self.text_area.toPlainText())
    





app = QApplication(sys.argv)

window = Notepad()


sys.exit(app.exec_())