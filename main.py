""" MainWindow is home base for executing hardware test routines."""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from beeperTest import beeperTest
from MainUI import Ui_MainWindow

class MainWindow:
    def __init__(self):
        pass
        
    """This function is connected to the Beeper Test button"""
    def run_beeper_test(self):
        beepertest = beeperTest()
        beepertest.start()
        
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    
    #connect button clicks to server routines
    ui.btnBeeperTest.clicked.connect(run_beeper_test)   
    
    window.show()
    sys.exit(app.exec_())
