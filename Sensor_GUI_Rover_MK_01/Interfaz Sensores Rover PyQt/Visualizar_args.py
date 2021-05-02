#!/usr/bin/python

#import datetime as dt
#import matplotlib; matplotlib.use("TkAgg")
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#import numpy as np
import Monitor_serial
import sys
import json_v3

#  Serial setup according to command line arguments

python_version = sys.version[0]

if len(sys.argv) != 2:
    print ("Wrong Number of Arguments!")
    print ("Please use format: python SensorTile_Animation_args.py SerialAddress")
else:
    address = sys.argv[1]

    if python_version == "2":
        python3 = False
    else:
        python3 = True

baud_rate = 9600
timeout = 2

#Serial Initialization
puertoSerial = Monitor_serial.serial_Monitor(address, baud_rate, timeout, python3)
puertoSerial.init_connection()

datos_recibidos = ''

while(1):
    data = puertoSerial.collect_data()
    if data != None:
        datos_recibidos = datos_recibidos + data
        #print(datos_recibidos)
        #print(data,end='')

    [cadenaExtraida, mensajeCompleto, datos_recibidos] = json_v3.CORTAR_JSON(datos_recibidos)
    if (mensajeCompleto):
      #print('Mensaje Completo')
      error = json_v3.REVISAR_JSON(cadenaExtraida)
      if (error):
        print('Mensaje Correcto Recibido')
        [nombres, valores] = json_v3.SEPARAR_MENSAJE_JSON(cadenaExtraida)
        print(nombres)
        print(valores)
        print('--------------------------')
      #else:
        #print('Error en la trama')
        #print(cadenaExtraida)
    #else:
      #print('Cadena Basura')
      #print(cadenaExtraida)
    
    #print(datos_recibidos)






# shutdown the system after closing the plot
puertoSerial.close_connection()

