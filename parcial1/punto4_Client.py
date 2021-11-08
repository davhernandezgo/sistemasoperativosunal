import socket
import asyncio
import os;


async def submit(i):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 3000
    sock.connect(('localhost',port))
    try:
        sock.send(i.encode())
    finally:
        sock.close()
async def receive_information():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 3000
    sock.connect(('localhost',port))
    try:
        data = sock.recv(4096)
        print(data.decode())
    finally:
        sock.close()
async def choose():
    os.chdir(r"C:\Users\USUARIO\Desktop\Parcial 1 So")
    with os.scandir(os.getcwd()) as archives:
        archives = [archives.name for archives in archives if archives.is_file() and archives.name.endswith('.txt')]
    file_selection = 1
    for i in archives:
        print(file_selection,i)
        file_selection+=1
    file_selection = int(input("choose the file to open\n"))
    return(archives[file_selection-1])
async def main():
    information = await choose()
    await submit(information)
    await asyncio.sleep(1)
    await receive_information()

asyncio.run(main())