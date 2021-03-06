from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys



class QWidgetDemos(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWidgets Demo")

        # test comment
        self.combobox = QComboBox()
      
        self.combobox.addItems(["Item 1", "Item 2", "Item 3"])

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.combobox)
        layout.addWidget(close_button)
        
        self.setLayout(layout)
        
        self.setFocus()
        self.combobox.currentIndexChanged.connect(self.selected)
        

    def selected(self):
        current_text = self.combobox.currentText()
        current_index = str(self.combobox.currentIndex())

        print(current_text + " at the index " + current_index)

app = QApplication(sys.argv)
dialog = QWidgetDemos()
dialog.show()
app.exec_()

