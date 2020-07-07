#Ex07-inputdialog
#Quand on clique sur le bouton, on demande de saisir:
#un nombre entier, un nombre décimal, puis un texte

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex07-inputdialog.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        #Quand on clique sur le pushButton, on appelle la méthode boutonOK
        self.pushButton.clicked.connect(self.boutonOk)
        self.show()             #affiche la fenêtre MainWindows

    def boutonOk(self):
        print('bouton cliqué')
        num,ok = QInputDialog.getInt(self,"Entier","Saisir un nombre entier")
        print("nombre entier saisi ",num,ok)
        dec,ok = QInputDialog.getDouble(self,"décimal","Saisir un nombre décimal")
        print("nombre décimal saisi ",dec,ok)
        text, ok = QInputDialog.getText(self, 'Text', 'Enter your name:')
        print("texte saisi ",text,ok)



app = QApplication(sys.argv)
window = MainWindows()
app.exec_()

