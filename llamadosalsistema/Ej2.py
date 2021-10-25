# un diccionario con las variables de entorno relativas al sistema. Se trata del diccionario environ.
import os
for variable, valor in os.environ.items():
    print ("%s: %s" % (variable, valor))
