import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import main_window

class Perelivanie(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  

def main():
    app = QApplication(sys.argv) 
    window = Perelivanie()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()