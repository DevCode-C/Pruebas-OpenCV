from PyQt5 import QtCore, QtGui, QtWidgets
import cv2

class CameraThread(QtCore.QThread):
    ImageUpdate = QtCore.pyqtSignal(QtGui.QImage)
    def run(self,Camara = 0):
        self.threadActive = True
        Capture = cv2.VideoCapture(Camara)
        while self.threadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image,1)
                ConvertToQtFormat =QtGui.QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QtGui.QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480,QtCore.Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

    def stop(self):
        self.ThreadActive = False
        self.quit()