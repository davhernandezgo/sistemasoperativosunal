import socket
import webbrowser


def open_page(address):
    webbrowser.open_new_tab(address)

def download_page():
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    puerto = 443
    socketClient.connect(('localhost', puerto))
    print("Conection is succesfull")
    data = socketClient.recv(4096)
    data = data.decode()
    page = open("client.html", "a")
    page.write(data)
    socketClient.close()
    print("the html code is\n" + data +
          "\n will be saved in client.html")
    webbrowser.open_new_tab("client.html")

download_page()