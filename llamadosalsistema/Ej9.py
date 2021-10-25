# Creacion y eliminacion de un directori
import os

print('Starting:', os.getcwd())
print('Moving up one:', os.pardir)
os.chdir(os.pardir)
print('After move:', os.getcwd())