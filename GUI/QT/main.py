from Ui_GUI1_Prueba import *

if __name__ == '__main__':
    app =QtWidgets.QApplication(sys.argv)
    GUI = Ventana()
    GUI.show()
    sys.exit(app.exec())