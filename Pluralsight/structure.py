# All PyQt modules start with Q so low chance of namespace conflicts.
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        
        layout = QGridLayout()
        
        self.label = QLabel("Hello World!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(self.label, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)

        self.setLayout(layout)

        # note self.close is a function but we don't add parenthesis
        # connect the event ot the widget
        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.label.setText)
                
    def changeTextLabel(self, text):
        self.label.setText(text)


app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()

# _ because exec is reserved keyword
app.exec_()
