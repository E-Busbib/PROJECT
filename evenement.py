from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QDialog
from PyQt5.QtCore import QTime
import sys

# Données simulées pour l'exemple de calcul de compatibilité
def calculer_plage_compatible(debut1, fin1, debut2, fin2):
    # Ici on simule une plage compatible entre 10:00 et 12:00 pour Paris et 04:00 - 06:00 pour New York
    return ("10:00", "12:00"), ("04:00", "06:00")

class EvenementDialog(QDialog):
    def __init__(self, resultats, parent=None):
        super().__init__(parent)
        uic.loadUi("evenement.ui", self)
        # resultats = (("10:00", "12:00"), ("04:00", "06:00"))
        self.labelResultat1.setText(f"Europe/Paris : {resultats[0][0]} - {resultats[0][1]}")
        self.labelResultat2.setText(f"America/New_York : {resultats[1][0]} - {resultats[1][1]}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interface.ui", self)

        self.calculerButton.clicked.connect(self.calculer)
        self.chargerSelectionButton.clicked.connect(self.charger_selection)
        self.historiqueList.itemDoubleClicked.connect(self.charger_selection)

    def calculer(self):
        tz1 = self.comboBoxTz1.currentText()
        tz2 = self.comboBoxTz2.currentText()

        debut1 = self.heureDebut1.time().toString("HH:mm")
        fin1 = self.heureFin1.time().toString("HH:mm")
        debut2 = self.heureDebut2.time().toString("HH:mm")
        fin2 = self.heureFin2.time().toString("HH:mm")

        resultat1, resultat2 = calculer_plage_compatible(debut1, fin1, debut2, fin2)

        item_text = f"{tz1} ({debut1}-{fin1}) & {tz2} ({debut2}-{fin2}) → Plage : {resultat1[0]} - {resultat1[1]} ({tz1}) & {resultat2[0]} - {resultat2[1]} ({tz2})"
        item = QListWidgetItem(item_text)
        item.setData(1000, (resultat1, resultat2))  # Stockage des résultats pour usage futur
        self.historiqueList.addItem(item)

    def charger_selection(self):
        item = self.historiqueList.currentItem()
        if item:
            resultats = item.data(1000)
            dialog = EvenementDialog(resultats, self)
            dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())