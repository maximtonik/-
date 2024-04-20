import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
import main_window
import level_window
import rules_window

class Perelivanie(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_level_window)
        
        self.pushButton_2.clicked.connect(self.show_rules_window)
        self.pushButton_3.clicked.connect(self.close)
        
    def show_level_window(self):
        self.level_window = LevelWindow()
        self.level_window.show()
    
    def show_rules_window(self):
        self.rules_window = RulesWindow()
        self.rules_window.show()
        

class LevelWindow(QMainWindow, level_window.Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_27.clicked.connect(self.menu_level)
    
    def menu_level(self):
        self.level_window = Perelivanie()
        self.level_window.show()
        
class RulesWindow(QMainWindow, rules_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.menu_level_rules)
    
    def menu_level_rules(self):
        self.level_window = Perelivanie()
        self.level_window.show()

def main():
    app = QApplication(sys.argv) 
    window = Perelivanie()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()