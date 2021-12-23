#Ex03-Affiche temperature
#affiche la température toutes les 2 secondes automatiquement

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys
import pyboard


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('afficheTemperature.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        self.timer = QTimer(self)   #déclaration du timer
        self.timer.timeout.connect(self.miseAJour) #déclenche la méthode mise à jour
        self.timer.start(2000)      #toutes les deux secondes (2000ms)
        self.pyb = pyboard.Pyboard('COM42')
        self.pyb.enter_raw_repl()
        self.show()             #affiche la fenêtre MainWindows

    def miseAJour(self):
        temp=self.pyb.execfile('temperature.py').decode("utf-8") #exécute le script python et retourne la température
        temp=temp.rstrip('\n') #retire le line feed
        print(temp)
        self.label.setText(temp+" °C") #on change le nom du label avec la temperature

    def closeEvent(self, event):
        print("quit")
        self.pyb.exit_raw_repl()


app = QApplication(sys.argv)
window = MainWindows()
app.exec_()



