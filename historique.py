from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HistoryWindow(object):
    def setupUi(self, HistoryWindow):
        HistoryWindow.setObjectName("HistoryWindow")
        HistoryWindow.resize(600, 400)
        HistoryWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        
        self.centralwidget = QtWidgets.QWidget(HistoryWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 50, 500, 250))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(50, 320, 150, 40))
        self.loadButton.setStyleSheet("background-color: rgb(0, 170, 255); font: 75 14pt 'Arial';")
        self.loadButton.setObjectName("loadButton")
        
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(400, 320, 150, 40))
        self.backButton.setStyleSheet("background-color: rgb(255, 0, 0); font: 75 14pt 'Arial';")
        self.backButton.setObjectName("backButton")

        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(225, 320, 150, 40))
        self.deleteButton.setStyleSheet("background-color: rgb(255, 170, 0); font: 75 14pt 'Arial';")
        self.deleteButton.setObjectName("deleteButton")
        
        HistoryWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(HistoryWindow)
        QtCore.QMetaObject.connectSlotsByName(HistoryWindow)

    def retranslateUi(self, HistoryWindow):
        _translate = QtCore.QCoreApplication.translate
        HistoryWindow.setWindowTitle(_translate("HistoryWindow", "Historique des plages horaires"))
        self.loadButton.setText(_translate("HistoryWindow", "Exporter en ICS"))
        self.backButton.setText(_translate("HistoryWindow", "Retour"))
        self.deleteButton.setText(_translate("HistoryWindow", "Supprimer"))



class HistoryWindow(QtWidgets.QMainWindow):

          
    def charger_historique(self):
        try:
            with open("historique.txt", "r", encoding="utf-8") as f:
                lignes = f.readlines()
                self.ui.listWidget.clear()
                for ligne in lignes:
                    self.ui.listWidget.addItem(ligne.strip())
        except FileNotFoundError:
            pass


    def supprimer_ligne_selectionnee(self):
        item = self.ui.listWidget.currentItem()
        if item:
            texte_a_supprimer = item.text()

            # Supprimer de l'affichage
            self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

            # Supprimer du fichier
            try:
                with open("historique.txt", "r", encoding="utf-8") as fichier:
                    lignes = fichier.readlines()
                with open("historique.txt", "w", encoding="utf-8") as fichier:
                    for ligne in lignes:
                        if ligne.strip() != texte_a_supprimer.strip():
                            fichier.write(ligne)
            except FileNotFoundError:
                print("Fichier historique.txt introuvable.")




    def __init__(self):
        super().__init__()
        self.ui = Ui_HistoryWindow()
        self.ui.setupUi(self)

        self.charger_historique()

        # (optionnel) Exemple de connexion du bouton "Retour"
        self.ui.backButton.clicked.connect(self.close)

        self.ui.deleteButton.clicked.connect(self.supprimer_ligne_selectionnee)

