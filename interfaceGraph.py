import sys
import socket 
import time
import threading
from PyQt6.QtWidgets import QApplication, QComboBox, QWidget, QLineEdit, QPushButton, QLabel

class IntGraph(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Le serveur de tchat")
        self.resize(330, 350)  
        
        self.Serveur = QLabel("Serveur :",self)
        self.Serveur.move(20, 20)
        self.Serveur.resize(150, 20)
        
        self.port = QLabel("port :",self)
        self.port.move(20, 50)
        self.port.resize(150, 20)
        
        self.nm_max = QLabel("nombre de client max :",self)
        self.nm_max.move(20, 80)
        self.nm_max.resize(150, 20)
        
        self.addr = QLineEdit("localhost", self)
        self.addr.move(150, 20)
        self.addr.resize(150, 20)
        
        self.numero_port = QLineEdit("4200",self)
        self.numero_port.move(150, 50)
        self.numero_port.resize(150, 20)
        
        self.nb_max = QLineEdit("5",self)
        self.nb_max.move(150, 80)
        self.nb_max.resize(150, 20)
        
        self.start_stop = QPushButton("démarrer le Serveur", self)
        self.start_stop.move(15, 110)
        self.start_stop.resize(300, 30)
        
        self.champ_texte = QLineEdit(self)
        self.champ_texte.move(15, 150)
        self.champ_texte.resize(300, 140)
        
        self.quitter = QPushButton("Quitter", self)
        self.quitter.move(15, 310)
        self.quitter.resize(300, 30)
        
        
        self.quitter.clicked.connect(self.close)
        self.start_stop.clicked.connect(self.demarrage)
        
    def demarrage(self):
        addr = self.addr.text()
        try: 
            numero_port = int(self.numero_port.text())
        except TypeError:
            print("ce n'est pas le bon type de variable ! ")
        finally:
            print("c'est tout bon ")
        server_socket = socket.socket()
        server_socket.bind((addr, numero_port))
        server_socket.listen(1)
        while 1: 
            conn, address = server_socket.accept()
            while 1:
                message = conn.recv(1024).decode()
                self.champ_texte.setText(f"[*] {message}\n")

        

    
    
    
if __name__ == "__main__":
    root = QApplication(sys.argv)
    fenetre = IntGraph()
    fenetre.show()
    sys.exit(root.exec())