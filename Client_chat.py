import socket
import select
import msvcrt

SERVER_IP = '127.0.0.0'
SERVER_PORT = 5555

def send_message(server_socket, message):
    print('\n')
def main():
    my_socket = socket.socket()
    my_socket.connect(SERVER_IP, SERVER_PORT)
    print('Pls enter commands:')

    message = ''
    
    while(True):
        if(msvcrt.kbhit()):
            k = msvcrt.getch()
            if(k == b'\r'):
                send_message(my_socket, message)
            else:
                print(k.decode(), flush=True, end='')
                message += k.decode()
main()