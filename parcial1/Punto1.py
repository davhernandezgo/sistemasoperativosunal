import os
import pandas as pd
from pandas import ExcelWriter

name_file = 'funciones.txt'
file = open(name_file, 'w')
file.write('Funciones sistema operativo:\nGestionar procesos o recursos para que los programas puedan ejecutarse de manera correcta.\n')
file.write('Administrar los puertos de entrada y salida, por ejemplo: micrófonos, altavoces, impresoras o el monitor.\n')
file.write('Garantizar la seguridad del ordenador, impidiendo el acceso a ciertos archivos o programas para el correcto funcionamiento del equipo.\n')
file.write('Administrar la memoria principal del dispositivo, de modo que aunque varios programas se pongan en marcha, cada uno cuente con una entrada de memoria independiente.\n')
file.write('Detectar errores, mantener la operatividad y controlar dispositivos, de manera que se eviten las interrupciones.')
file.close()
if name_file in os.listdir("."):
    print ("Archivo creado en la ruta: \n\t{0}/{1}".format(
        os.getcwd(), name_file))
else:
    print ("El archivo no fue creado!!!\n")

df = pd.DataFrame({'Id': [1, 3, 2, 4,5],
                   'Funcion': ['Gestionar procesos o recursos para que los programas puedan ejecutarse de manera correcta', 'Administrar los puertos de entrada y salida, por ejemplo: micrófonos, altavoces, impresoras o el monitor',
                    'Garantizar la seguridad del ordenador, impidiendo el acceso a ciertos archivos o programas para el correcto funcionamiento del equipo'
                    , 'Administrar la memoria principal del dispositivo, de modo que aunque varios programas se pongan en marcha, cada uno cuente con una entrada de memoria independiente',
                    'Detectar errores, mantener la operatividad y controlar dispositivos, de manera que se eviten las interrupciones.'],})
df = df[['Id', 'Funcion']]
writer = ExcelWriter('C:/Users/USUARIO/Desktop/Parcial 1 So/funciones.xlsx')
df.to_excel(writer, 'Hoja de funciones', index=False)
writer.save()
