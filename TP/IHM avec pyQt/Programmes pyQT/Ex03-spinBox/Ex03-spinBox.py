#Ex03-spinBox
#Quand on clique sur le bouton, on affiche le résultat du calcul d'un nombre d'une spinbox

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex03-spinBox.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        #Quand on clique sur le pushButton, on appelle la fonction boutonOK
        self.pushButton.clicked.connect(self.boutonOk)
        self.show()             #affiche la fenêtre MainWindows

    def boutonOk(self):
        print('bouton cliqué')
        txt=self.lineEdit.text()    #récupère le texte de lineEdit
        print('texte saisi:',txt,type(txt)) #affiche dans la console le texte et le type
        b=self.spinBox.value()  #récupère le nombre de la spinbox
        print('valeur de la spin box',b) #‗affiche cette valeur dans la console
        if txt.isnumeric():     #le texte est il un chiffre ?
            a=int(txt)          #conversion en entier
            a=a+b              #ajoute la valeur b
            self.label.setText(str(a)) #affiche le résulat
        else:
            self.label.setText("nombre svp")


app = QApplication(sys.argv)
window = MainWindows()
app.exec_()

