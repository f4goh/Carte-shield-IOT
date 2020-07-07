#Ex10-painter
#tracé de formes géométriques

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui,uic
import sys


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        uic.loadUi('Ex10-painter.ui', self)  #chargement du formulaire XML
        self.setFixedSize(self.size())  #la fenêtre principale n'est pas modifiable
        self.show()             #affiche la fenêtre MainWindows

    def paintEvent(self, event):
        painter = QPainter(self)
        trace=1		#N° du tracé

        if trace==1:
            #Affichage d'une image
            pic = QPixmap("logo.png") #chargement
            painter.drawPixmap(10,10, pic) #affichage aux coordonnées
        elif trace==2:
            #tracé d'un rectangle
            painter.setPen(QPen(Qt.red, 5)) #definir un crayon
            painter.setBrush(Qt.green) # definir un remplissage
            painter.drawRect(0, 0, 100, 100) #tracé
        elif trace==3:
            #tracé d'une ellipse
            painter.setPen(QPen(Qt.blue, 3)) #definir un crayon
            painter.setBrush(QColor(255, 255, 0)) #couleur de remplissage RGB
            painter.drawEllipse(50,30,80,40) #tracé
        elif trace==4:
            #tracé de polygone
            points = [      #definir les 4 points du polygone
                QPoint(10,10),
                QPoint(10,100),
                QPoint(100,10),
                QPoint(100,100)
                ]
            painter.setPen(QPen(Qt.red, 5)) #crayon rouge largeur 5
            painter.setBrush(Qt.green) # couleur du remplissage
            poly = QPolygon(points) #instancier un polygone a partir de points
            painter.drawPolygon(poly)   #tracé
        elif trace==5:
            #tracé de rectangle avec gradiant
            painter.setPen(QPen(Qt.black,  5, Qt.SolidLine))
            grad = QLinearGradient(10, 10, 50, 60)
            painter.setBrush(QBrush(grad))
            painter.drawRect(10, 10, 50, 60)
        elif trace==6:
            #tracé de rectangle contour en pointillés
            painter.setPen(QPen(Qt.black,  5, Qt.DotLine)) #crayon noir largeur 5 en pointillés
            painter.setBrush(QBrush(Qt.red, Qt.CrossPattern)) #remplissage rouge
            painter.drawRect(10, 20, 60, 50) #tracé
        elif trace==7:
            #Affichage de texte
            painter.setPen(QColor(255, 0, 0)) #couleur du crayon
            painter.setFont(QFont('Arial', 20)) #police
            painter.drawText(self.rect(), Qt.AlignCenter, "titi") #affichage au centre de la fenetre
            painter.drawText(20,30, "toto") #affichage aux coordonées
        elif trace==8:
            #tracé de points
            painter.setPen(QColor(0, 0, 255)) #couleur du crayon
            for x in range(0,50,2):
                painter.drawPoint(x+10, 20)



app = QApplication(sys.argv)
window = MainWindows()
app.exec_()

