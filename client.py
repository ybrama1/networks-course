import socket
my_socket = socket.socket()
my_socket.connect(("127.0.0.1", 8820))

while(True):
    massege = input("enter a massege: ")
    lengh = str(len(massege))
    lengh = lengh.zfill(4)
    my_socket.send((lengh + massege).encode())

    lengh = my_socket.recv(4).decode()
    print(my_socket.recv(int(lengh)).decode())

    data = my_socket.recv(1024).decode()
    print("The server sent " + data)
my_socket.close()