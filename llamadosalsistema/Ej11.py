#El valor de salida del shell que ejecuta el programa empaquetado en un número de 16 bits,
# con el byte alto el estado de salida y el byte bajo el número de señal que causó la muerte del proceso, o cero.
import os
import time

os.system('date; (sleep 3; date) &')
time.sleep(5)