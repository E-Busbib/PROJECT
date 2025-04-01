import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Deuxième fenêtre")
        self.setGeometry(200, 200, 300, 200)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fenêtre principale")
        self.setGeometry(100, 100, 400, 300)
        
        self.button = QPushButton("Ouvrir une nouvelle fenêtre")
        self.button.clicked.connect(self.open_new_window)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        container.setLayout(layout)

        self.setCentralWidget(container)

        # Garde une référence pour éviter que la fenêtre se ferme immédiatement
        self.second_window = None

    def open_new_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
