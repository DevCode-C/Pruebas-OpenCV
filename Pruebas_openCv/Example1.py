import cv2 #Importamos la libreria open cv 
import socket

cap = cv2.VideoCapture(0) # Se usa una direccion IP local para una prueba pre elimiar de transmision de video

while(1):
    ret, frame = cap.read()

    cv2.imshow('Camara',frame)

    if cv2.waitKey(1) & 0xFF  == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()