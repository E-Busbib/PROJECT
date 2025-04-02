from PyQt5.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget, QCompleter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPalette


class ComboBoxSearch(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recherche dans une ComboBox")
        self.setGeometry(100, 100, 300, 100)

        # Création de la comboBox
        self.comboBox = QComboBox(self)
        self.comboBox.setEditable(True)  # Permet de taper dans la ComboBox

        # Liste des éléments
        items = ["Paris", "Londres", "Berlin", "Madrid", "Rome", "New York"]
        self.comboBox.addItems(items)

        # Ajout de l'autocomplétion
        completer = QCompleter(items, self.comboBox)
        completer.setCaseSensitivity(False)  # Ignorer la casse
        completer.setFilterMode(Qt.MatchContains)  # Recherche même si le texte est au milieu
        self.comboBox.setCompleter(completer)

        # Mise en page
        layout = QVBoxLayout()
        layout.addWidget(self.comboBox)
        self.setLayout(layout)

        self.comboBox.setStyleSheet("""
            QComboBox {
                border: 2px solid #5c6bc0;
                border-radius: 5px;
                padding: 5px;
                background-color: white;
                color: #333;
                font-size: 14px;
            }
            QComboBox:hover {
                border-color: #3949ab;
            }
            QComboBox::drop-down {
                border: 0px;
                background: transparent;
            }
            QComboBox::down-arrow {
                image: url(down-arrow.png);  /* Ajoute une icône personnalisée */
                width: 12px;
                height: 12px;
            }
            QComboBox QAbstractItemView {
                border: 1px solid #3949ab;
                selection-background-color: #7986cb;
            }
        """)

        

        self.comboBox.setItemIcon(0, QIcon("icon.png"))  # Change l'icône du premier élément

        

        palette = self.comboBox.palette()
        palette.setColor(self.comboBox.backgroundRole(), Qt.white)
        palette.setColor(self.comboBox.foregroundRole(), Qt.black)
        self.comboBox.setPalette(palette)




if __name__ == "__main__":
    app = QApplication([])
    window = ComboBoxSearch()
    window.show()
    app.exec_()
