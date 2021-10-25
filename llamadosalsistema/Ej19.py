# Devuelve una tupla que representa el principio y el final del nombre de ruta especificado..
import os

path = '/home/User/Desktop/file.txt'
head_tail = os.path.split(path)
print("Head: ", head_tail[0])
print("Tail: ", head_tail[1], "\n")