from PyQt5 import QtCore, QtGui, QtWidgets
from ics import Calendar, Event
from datetime import datetime

class Ui_HistoryWindow(object):
    def setupUi(self, HistoryWindow):
        HistoryWindow.setObjectName("HistoryWindow")
        HistoryWindow.setFixedSize(600, 400)
        HistoryWindow.setStyleSheet("background-color: white;")
        
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


    def exporter_en_ics(self):
        item = self.ui.listWidget.currentItem()
        if not item:
            QtWidgets.QMessageBox.warning(self, "Aucune sélection", "Veuillez sélectionner une ligne dans l'historique.")
            return

        ligne = item.text()
        try:
            # Séparation en deux fuseaux
            part1, part2 = ligne.split("⇄")
            fuseau1, horaire1 = part1.strip().split(": ")
            fuseau2, horaire2 = part2.strip().split(": ")
            debut1, fin1 = horaire1.split(" - ")
            debut2, fin2 = horaire2.split(" - ")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erreur de format", f"Impossible d'interpréter la ligne sélectionnée.\n{e}")
            return

        

        


        # Demander le nom de l'événement
        nom_evenement, ok = QtWidgets.QInputDialog.getText(self, "Nom de l'événement", 
            "Entrez un nom pour votre événement :")
        if not ok or not nom_evenement.strip():
            nom_evenement = "Rendez-vous"
        

        # Demander à l'utilisateur dans quel fuseau il se trouve
        fuseau_choisi, ok = QtWidgets.QInputDialog.getItem(self, "Fuseau horaire", 
            "Dans quel fuseau êtes-vous ?", [fuseau1, fuseau2], 0, False)
        if not ok:
            return

        # Obtenir la plage correspondant au fuseau choisi
        if fuseau_choisi == fuseau1:
            heure_min, heure_max = debut1.strip(), fin1.strip()
        else:
            heure_min, heure_max = debut2.strip(), fin2.strip()

        # Demander une date
        date_str, ok = QtWidgets.QInputDialog.getText(self, "Date de l'événement", 
            "Entrez une date (format AAAA-MM-JJ) :")
        if not ok:
            return

        # Vérification de la date
        try:
            date = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
        except:
            QtWidgets.QMessageBox.critical(self, "Date invalide", "Format de date incorrect.")
            return

        # Heure de début
        heure_debut_str, ok = QtWidgets.QInputDialog.getText(self, "Heure de début", 
            f"Heure de début entre {heure_min} et {heure_max} (HH:MM) :")
        if not ok:
            return

        # Heure de fin
        heure_fin_str, ok = QtWidgets.QInputDialog.getText(self, "Heure de fin", 
            f"Heure de fin entre {heure_debut_str} et {heure_max} (HH:MM) :")
        if not ok:
            return

        # Vérifications
        try:
            hmin = datetime.strptime(heure_min, "%H:%M").time()
            hmax = datetime.strptime(heure_max, "%H:%M").time()
            hstart = datetime.strptime(heure_debut_str, "%H:%M").time()
            hend = datetime.strptime(heure_fin_str, "%H:%M").time()
        except:
            QtWidgets.QMessageBox.critical(self, "Heures invalides", "Format d’heure incorrect.")
            return

        if not (hmin <= hstart < hend <= hmax):
            QtWidgets.QMessageBox.critical(self, "Heures hors plage", "Les horaires choisis ne sont pas dans la plage autorisée.")
            return

        # Création de l'événement ICS
        start_dt = datetime.combine(date, hstart)
        end_dt = datetime.combine(date, hend)

        e = Event()
        e.name = nom_evenement.strip()
        e.begin = start_dt
        e.end = end_dt
        e.description = f"Plage choisie dans {fuseau_choisi}"

        c = Calendar()
        c.events.add(e)

        # Sauvegarde
        # Ouvrir une fenêtre de sauvegarde pour choisir dossier + nom du fichier
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog  # optionnel si tu veux forcer le style Qt
        chemin_fichier, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Enregistrer l'événement",
            "evenement.ics",  # nom par défaut
            "Fichiers ICS (*.ics)",
            options=options
        )

        if chemin_fichier:
            # S'assurer que l'extension est bien .ics
            if not chemin_fichier.lower().endswith('.ics'):
                chemin_fichier += ".ics"

            with open(chemin_fichier, "w", encoding="utf-8") as f:
                f.writelines(c)

            QtWidgets.QMessageBox.information(self, "Succès", f"Fichier ICS sauvegardé dans :\n{chemin_fichier}")
        else:
            QtWidgets.QMessageBox.information(self, "Annulé", "Sauvegarde annulée.")




    def __init__(self):
        super().__init__()
        self.ui = Ui_HistoryWindow()
        self.ui.setupUi(self)

        self.charger_historique()

        # (optionnel) Exemple de connexion du bouton "Retour"
        self.ui.backButton.clicked.connect(self.close)

        self.ui.deleteButton.clicked.connect(self.supprimer_ligne_selectionnee)

        self.ui.loadButton.clicked.connect(self.exporter_en_ics)


