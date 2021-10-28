import socket

mySocket= socket.socket()
mySocket.bind(('localhost',7000))
mySocket.listen(5)
while True:
    conection, address=mySocket.accept()
    print("New Conection")
    print (address)
    data="Hello customer"
    conection.send(data.encode())
    conection.close()