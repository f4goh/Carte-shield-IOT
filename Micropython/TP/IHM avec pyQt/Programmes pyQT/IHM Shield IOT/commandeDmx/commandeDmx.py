#Ex04-commande dmx
#controle un projecteur  RGB simple à leds 4 canaux

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys
import pyboard


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('commandeDmx.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        #Quand on clique sur le pushButton, on appelle la méthode bouton_color_picker
        self.verticalSlider_Red.valueChanged.connect(self.potentiometre)
        self.verticalSlider_Green.valueChanged.connect(self.potentiometre)
        self.verticalSlider_Blue.valueChanged.connect(self.potentiometre)
        self.verticalSlider_Dimmer.valueChanged.connect(self.potentiometre)
        self.pyb = pyboard.Pyboard('COM42')
        self.pyb.enter_raw_repl()
        self.show()             #affiche la fenêtre MainWindows

    def potentiometre(self):
        red=self.verticalSlider_Red.value()    #récupère la valeur du rouge
        green=self.verticalSlider_Green.value()    #récupère la valeur du vert
        blue=self.verticalSlider_Blue.value()    #récupère la valeur du bleu
        dimmer=self.verticalSlider_Dimmer.value()    #récupère la valeur du dimmer
        print(red,green,blue,dimmer)
        self.pyb.exec('couleur = ({}, {}, {},{})'.format(red,green,blue,dimmer))  #parametre de couleur dans le script
        self.pyb.execfile('dmx32.py')           #execute le script

    def closeEvent(self, event):
        print("quit")
        self.pyb.exit_raw_repl()
        self.pyb.close()



app = QApplication(sys.argv)
window = MainWindows()
app.exec_()

