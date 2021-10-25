# se utilizan para referirse a los directorios actuales y principales de manera portable.
import os

print('Starting:', os.getcwd())
print('Moving up one:', os.pardir)
os.chdir(os.pardir)
print('After move:', os.getcwd())