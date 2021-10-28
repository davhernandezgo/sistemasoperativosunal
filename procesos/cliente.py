import socket

mySocket=socket.socket()
mySocket.connect(('localhost',7000))
data="hello, I am the customer"
mySocket.send(data.encode())
answer=mySocket.recv(1024)
print(answer)
mySocket.close()