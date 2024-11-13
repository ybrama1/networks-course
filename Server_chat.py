import socket
import select

MAX_MSG_LENGTH = 1024
SERVER_PORT = 5555
SERVER_IP = '0.0.0.0'

def print_client_sockets(client_sockets):
    for i in client_sockets:
        print('\t', i.getpeername())
def main():

    print('restart the server')
    server_socket = socket.socket()
    server_socket.bind(SERVER_IP, SERVER_PORT)
    server_socket.listen()

    print('listening...')
    client_sockets = []
    messages_to_send = []

    while(True):
        rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])
        for current_socket in rlist:
            if current_socket is server_socket:
                connection, client_address = current_socket.accept()
                print("New client joined!", client_address)
                client_sockets.append(connection)
                print_client_sockets(client_sockets)
            else:
                pass
        for message in messages_to_send:
            pass