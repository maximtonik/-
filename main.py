import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
import main_window
import difficult_level_window, easy_level_window, medium_level_window, hard_level_window
import rules_window

class Perelivanie(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_difficult_level_window)
        
        self.pushButton_2.clicked.connect(self.show_rules_window)
        self.pushButton_3.clicked.connect(self.close)
        
    def show_difficult_level_window(self):
        self.difficult_level_window = DifficultLevelWindow()
        self.difficult_level_window.show()
        
    
    def show_rules_window(self):
        self.rules_window = RulesWindow()
        self.rules_window.show()
        self.setCentralWidget(self.rules_window)
        
        

class DifficultLevelWindow(QMainWindow, difficult_level_window.Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_27.clicked.connect(self.show_main_menu_level)
        self.pushButton_5.clicked.connect(self.show_easy_menu_level)
        self.pushButton_4.clicked.connect(self.show_medium_menu_level)
        self.pushButton_3.clicked.connect(self.show_hard_menu_level)
    
    def show_main_menu_level(self):
        self.level_window = Perelivanie()
        self.level_window.show()
    
    def show_easy_menu_level(self):
        self.easy_level_window = EasyDifficultLevelWindow()
        self.easy_level_window.show()
    
    def show_medium_menu_level(self):
        self.medium_level_window = MediumDifficultLevelWindow()
        self.medium_level_window.show()
    
    def show_hard_menu_level(self):
        self.hard_level_window = HardDifficultLevelWindow()
        self.hard_level_window.show()
        
class RulesWindow(QMainWindow, rules_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.menu_level_rules)
    
    def menu_level_rules(self):
        self.level_window = Perelivanie()
        self.level_window.show()

class EasyDifficultLevelWindow(QMainWindow, easy_level_window.Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_easy_level_27.clicked.connect(self.main_menu_level)
        # добавление уровней
    
    def main_menu_level(self):
        self.level_window = DifficultLevelWindow()
        self.level_window.show()

class MediumDifficultLevelWindow(QMainWindow, medium_level_window.Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_medium_level_27.clicked.connect(self.main_menu_level)
        # добавление уровней
    
    def main_menu_level(self):
        self.level_window = DifficultLevelWindow()
        self.level_window.show()

class HardDifficultLevelWindow(QMainWindow, hard_level_window.Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_hard_level_27.clicked.connect(self.main_menu_level)
        # добавление уровней
    
    def main_menu_level(self):
        self.level_window = DifficultLevelWindow()
        self.level_window.show()
def main():
    app = QApplication(sys.argv) 
    window = Perelivanie()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()