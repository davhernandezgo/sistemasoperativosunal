import hashlib
import os
from os import listdir
from os.path import isdir, islink
for filename in listdir("."):
    if not isdir(filename) and not islink(filename):
        try:
            f = open(filename, "rb")
        except IOError as e:
            print(e)
        else:
            archivo=open('Hash.txt','a')
            data = f.read()
            f.close()
            print("** {} **".format(filename))
            h = hashlib.sha1()
            h.update(data)
            try:
                hexdigest = h.hexdigest()
            except TypeError:
                hexdigest = h.hexdigest(256)
            archivo.write("sha1: "+hexdigest+'\n')
            print("sha1: {}".format(hexdigest))
            print()