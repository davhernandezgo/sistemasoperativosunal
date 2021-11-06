import socket
import ssl
import asyncio

protocol = ssl.create_default_context()
url = "www.buda.com"
port = 443

function1 = b"GET /api/v2/markets HTTP/1.0\r\nHost: www.buda.com\r\n\r\n"
function2 = b"GET /api/v2/markets/eth-btc/ticker HTTP/1.0\r\nHost: www.buda.com\r\n\r\n"
function3 = b"GET /api/v2/markets/eth-btc/trades HTTP/1.0\r\nHost: www.buda.com\r\n\r\n"
async def writer(message):
    for i in range(0,len(message),1):
        if message[i]=='{':
            file = open("datos.txt", "a")
            file.write(message[i:]+"\n")
            break

async def request(route):
    socketCliente = protocol.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=url)
    socketCliente.connect((url, port))
    socketCliente.send(route)
    message = socketCliente.recv(4096)
    await writer(message.decode())
    print(message.decode())

async def main():
    task1 = asyncio.create_task(request(function3))
    await asyncio.sleep(1)
    await task1
    task2 = asyncio.create_task(request(function1))
    await asyncio.sleep(1)
    await task2
    task3 = asyncio.create_task(request(function2))
    await asyncio.sleep(1)
    await task3

    print("End of the connection")

asyncio.run(main())