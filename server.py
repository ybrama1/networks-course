import socket
import time
import glob
import os
import shutil
import subprocess
import pyautogui

def sent_DIR(massege, client_socket):
    """show all the files in a folder"""
    lengh = str(len(str(massege)))
    lengh = lengh.zfill(4)
    send = ''
    for i in massege:
        send += i + "\n"
    client_socket.send((lengh + send).encode())

def sent_DELETE(msg, client_socket):
    """ delete a file """
    os.remove('C:\\Networks\\work\\todelete\\' + msg + '.txt')

    reply = msg + ".txt was deleted."
    send_reply(reply, client_socket)

def sent_COPY(msg, client_socket):
    """ copy file from one location to another on the server """
    (name1, name2) = msg.split(',')
    shutil.copy("C:\\Networks\\work\\tocopy\\" + name1 + ".txt" , "C:\\Networks\\work\\" + name2)
    
    reply = name1 + ".txt was coppied."
    send_reply(reply, client_socket)

def sent_EXECUTE(msg, client_socket):
    """ open a app on the server computer """
    subprocess.call(msg)

    reply = msg + " was opened."
    send_reply(reply, client_socket)

def sent_TAKE_SCREENSHOT(client_socket):
    """ take a screenshot and save it as "coolscreenshot.jpg" """
    image = pyautogui.screenshot()
    image.save("C:\\Networks\\work\\tocopy\\coolscreenshot.jpg")

    reply = "SCREENSHOTTED"
    send_reply(reply, client_socket)

def sent_SEND_PHOTO(client_socket):
    """ send the screenshot "coolscreenshot.jpg" to the client """
    openfile = open("C:\\Networks\\work\\tocopy\\coolscreenshot.jpg", 'rb')
    file = openfile.read()
    len_file = str(len(file))
    len_len_file = str(len(len_file))
    len_len_file = len_len_file.zfill(4)
    client_socket.send((len_len_file + len_file + str(file)).encode())

    openfile.close()

def send_reply(msg, client_socket):
    """ send a reply to the client by msg and client socket """
    lengh = str(len(msg))
    lengh = lengh.zfill(4)
    client_socket.send((lengh + msg).encode())

def main():
    """
    this program is a sever. the client can ask questions to the server.
    the questions are:
        DIR for shows all the files in a folder
        DELETE to delete a file
        COPY to copy a file
        EXECUTE to open app
        TAKE_SCREENSHOT
        SEND_SKREENSHOT
    """

    server_socket = socket.socket()
    server_socket.bind(("0.0.0.0", 8820))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")
    while(True):
        lengh = client_socket.recv(4).decode()
        massege = client_socket.recv(int(lengh)).decode()
        print("messege: " + massege)

        if(massege == "EXIT"):
            break
        (op, massege) = massege.split()
        if(op == "DIR"):
            files_list = (glob.glob(massege + "\*.*"))
            sent_DIR(files_list, client_socket)
        elif(op == "DELETE"):
            sent_DELETE(massege, client_socket)
        elif(op == "COPY"):
            sent_COPY(massege, client_socket)
        elif (op == "EXECUTE"):
            sent_EXECUTE(massege, client_socket)
        elif (op == "TAKE_SCREENSHOT"):
            sent_TAKE_SCREENSHOT(client_socket)
        elif (op == "SEND_PHOTO"):
            sent_SEND_PHOTO(client_socket)
    client_socket.close()
    server_socket.close()
main()