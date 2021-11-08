import socket
import os
import asyncio

async def receive_information():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 3000
    sock.bind(('localhost',port))
    sock.listen(1)
    while True:
        connetcion, address = sock.accept()
        try:
            data = connetcion.recv(4096)
            message = data.decode()
        finally:
            connetcion.close()
        return message
async def submit_information(i):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 3000
    sock.bind(('localhost',port))
    sock.listen(1)
    while True:
        con, addr = sock.accept()
        try:
            f = open(i, 'rb')
            contenido = f.read()
            con.sendall(contenido)
            f.close()
            break
        finally:
            con.close()
async def main():
    os.chdir(r"C:\Users\USUARIO\Desktop\Parcial 1 So")
    information = await receive_information()
    print(information)
    await submit_information(information)

asyncio.run(main())