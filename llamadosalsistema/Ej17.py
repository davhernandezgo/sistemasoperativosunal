#Crear un enlace simbolico.
import os

link_name = '/tmp/' + os.path.basename(__file__)
print('Creating link {} -> {}'.format(link_name, __file__))
os.symlink(__file__, link_name)