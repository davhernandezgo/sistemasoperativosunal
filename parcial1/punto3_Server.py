import socket
import asyncio

ejecucion = True
async def send_page(contenido):
    socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 443
    socketServidor.bind(('localhost', port))
    socketServidor.listen(1)
    connection, address = socketServidor.accept()
    connection.send(contenido.encode())
    print("html has been sent to the client")
    connection.close()
    socketServidor.close()


async def main():
    file = open("punto3.html", "r")
    content = file.read()
    task = asyncio.create_task(send_page(content))


asyncio.run(main())
