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
        self.loadButton.setGeometry(QtCore.QRect(50, 320, 200, 40))
        self.loadButton.setStyleSheet("background-color: rgb(0, 170, 255); font: 75 14pt 'Arial';")
        self.loadButton.setObjectName("loadButton")
        
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(350, 320, 200, 40))
        self.backButton.setStyleSheet("background-color: rgb(255, 0, 0); font: 75 14pt 'Arial';")
        self.backButton.setObjectName("backButton")
        
        HistoryWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(HistoryWindow)
        QtCore.QMetaObject.connectSlotsByName(HistoryWindow)

    def retranslateUi(self, HistoryWindow):
        _translate = QtCore.QCoreApplication.translate
        HistoryWindow.setWindowTitle(_translate("HistoryWindow", "Historique des plages horaires"))
        self.loadButton.setText(_translate("HistoryWindow", "Charger la sélection"))
        self.backButton.setText(_translate("HistoryWindow", "Retour"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HistoryWindow = QtWidgets.QMainWindow()
    ui = Ui_HistoryWindow()
    ui.setupUi(HistoryWindow)
    HistoryWindow.show()
    sys.exit(app.exec_())
