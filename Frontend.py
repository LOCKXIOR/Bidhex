from Backend import Transfo
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from os import*

class UI:
    def __init__(self,app):
        
        a=250
        b=75
        longueur=800
        largeur=800
        
        self.logique=Transfo("Transformateur dans le fichier Backend")
        
        self.tout_mode={"binaire": self.bi}
        self.mode_actuel="normale"
        
        self.app=app
        self.window=QWidget()
        self.window.setFixedSize(longueur,largeur)
        self.window.setWindowTitle("Transformateur")
        
        self.logo=path.join(path.dirname(__file__),"social.png")
        self.window.setWindowIcon(QIcon(self.logo))
        
        self.text1=QLabel("Transformateur de valeurs")
        self.text2=QLabel("")
        self.text3=QLabel("")
        self.carré=QLabel("")

        self.carré.setObjectName("carré")
        
        self.bouton1=QPushButton("Binaire")
        self.bouton1.setFixedSize(a,b)
        self.bouton1.clicked.connect(self.bi)
        
        self.bouton2=QPushButton("Hexadecimal")
        self.bouton2.setFixedSize(a,b)
        self.bouton2.clicked.connect(self.hexa)
        
        self.bouton3=QPushButton("Couleur")
        self.bouton3.setFixedSize(a,b)
        self.bouton3.clicked.connect(self.deci_couleur)
        
        self.entrée=QLineEdit()
        self.entrée.setPlaceholderText("Entre ton nombre")
        self.entrée.setMaximumWidth(1000)
        
        self.layout=QVBoxLayout()
        self.layout_bout=QVBoxLayout()
        self.layout.addWidget(self.text1, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.carré, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.entrée)
        self.layout.addWidget(self.bouton1, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.bouton2, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.bouton3, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.text2, alignment=Qt.AlignCenter)
        
        
        self.window.setLayout(self.layout)
        
        
    def get_nombre(self):
        try:
            self.nombre=int(self.entrée.text().strip().replace(" ",""))
            self.entrée.clear()
            self.text2.setText("")
            self.carré.setText("")
        except Exception as e0:
            self.text2.setText("Erreur 1")
            self.text1.setText(f"Erreur 1: {e0}")
            self.carré.setText("")
        
    def show(self):
        self.window.show()
        self.app.exec_()
    
    def bi(self):
        try:
            nombre=int(self.entrée.text().strip().replace(" ",""))
            self.entrée.clear()
            self.text1.setText(f"Transformation décimale-binaire")
            self.text2.setText("")
            self.carré.setText(f"'{nombre}' devient '{self.logique.binaire(nombre)}'")
        except Exception as e1:
            self.entrée.clear()
            self.text2.setText("Erreur 2")
            self.text1.setText(f"Erreur 2: {e1}")
            self.carré.setText("")
    
    def hexa(self):
        try:
            nombre=int(self.entrée.text().strip().replace(" ",""))
            self.entrée.clear()
            self.text1.setText(f"Transformation décimale-hexadecimal")
            self.text2.setText("")
            self.carré.setText(f"'{nombre}' devient '{self.logique.hexadecimal(nombre)}'")
        except Exception as e2:
            self.entrée.clear()
            self.text2.setText("Erreur 3")
            self.text1.setText(f"Erreur 3: {e2}")
            self.carré.setText("")
        
    def deci_couleur(self):
        try:
            couleur_deci=int(self.entrée.text().strip().replace(" ",""))
            self.text1.setText("Couleur en hexadécimal")
            self.text2.setText("")
            a=self.logique.deci_color(couleur_deci)
            self.carré.setText(a)
            self.entrée.clear()
        except Exception as e3 :
            self.entrée.clear()
            self.text2.setText("Erreur 4")
            self.text1.setText(f"Erreur 4: {e3}")
             
        
if __name__ == "__main__":
    app=QApplication([])
    app.setStyleSheet("""
        QWidget {
        background-color: #7A89BD
        }
        QLabel {
            font-family : Times new roman;
            font-style : italic;
            font-size : 14pt;
            text-align : justify
        }
        QPushButton {
            font-family : Times new roman;
            font-style : italic;
            font-size : 10pt;
            border : 1px solid;
            border-radius : 15px;
            color : #ffffff;
            background-color : #001A36
        }
        QPushButton:hover {
            background-color : #001224
        }
        QLineEdit {
            background-color: #ffffff;
            border: 2px solid #ccc;
            border-radius: 6px;        
            padding: 5px 10px;
            font-size: 16px;
        }
        QLineEdit:focus {
            border: 1px solid #001A36; 
        }
""")
    a=UI(app)
    a.show()
    

        