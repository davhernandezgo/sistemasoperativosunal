#Los códigos de error definidos por el sistema operativo y administrados en el módulo errno se pueden traducir a
# cadenas de mensajes usando strerror().
import errno
import os

for num in [errno.ENOENT, errno.EINTR, errno.EBUSY]:
    name = errno.errorcode[num]
    print('[{num:}] {name:}: {msg}'.format(
        name=name, num=num, msg=os.strerror(num)))