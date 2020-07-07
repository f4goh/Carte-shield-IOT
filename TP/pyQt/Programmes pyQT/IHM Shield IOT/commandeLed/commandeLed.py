#Ex01-commande de led via pyQT et REPL
#Commande la led avec deux push bouttons on et off

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys
import pyboard


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('commandeLed.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        #Quand on clique sur les pushButton, on appelle les méthodes respectives
        self.pushButton_LedOn.clicked.connect(self.boutonOn)
        self.pushButton_LedOff.clicked.connect(self.boutonOff)
        self.pyb = pyboard.Pyboard('COM42')
        self.pyb.enter_raw_repl()
        self.show()             #affiche la fenêtre MainWindows

    def boutonOn(self):
        print("on")
        self.pyb.execfile('led_on.py')

    def boutonOff(self):
        print("off")
        self.pyb.execfile('led_off.py')

    def closeEvent(self, event):
        print("quit")
        self.pyb.exit_raw_repl()


app = QApplication(sys.argv)
window = MainWindows()
app.exec_()

