#Ex02-Colorpicker
#Choisir une couleur dans une palette, puis allume les leds neopixels

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys
import pyboard


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('commandeNeopixels.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        #Quand on clique sur le pushButton, on appelle la méthode bouton_color_picker
        self.pushButton.clicked.connect(self.bouton_color_picker)
        self.pyb = pyboard.Pyboard('COM42')
        self.pyb.enter_raw_repl()
        self.show()             #affiche la fenêtre MainWindows

    def bouton_color_picker(self):
        color = QColorDialog.getColor()     #choisir une couleur
        print(color.name())
        self.pyb.exec('couleur = ({}, {}, {})'.format(color.red(),color.green(),color.blue()))  #parametre de couleur dans le script
        self.pyb.execfile('neopixels.py')           #execute le script

    def closeEvent(self, event):
        print("quit")
        self.pyb.exit_raw_repl()


app = QApplication(sys.argv)
window = MainWindows()
app.exec_()



