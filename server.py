import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))

server.listen()

while True :
    user, adress = server.accept()

    user.send(input().encode("utf-8"))
    data = user.recv(1024)
    print(data.decode("utf-8"))
