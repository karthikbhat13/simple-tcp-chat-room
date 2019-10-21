import socket
import sys
import select

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    con_list = [sys.stdin, client_socket]

    while 1:
        read_sock, write_sock, err_sock = select.select(con_list, [], [])

        for sock in read_sock:
            if sock == client_socket:
                data = client_socket.recv(1024).decode()

                print('Received from server: ' + data)  # show in terminal

            else:
                message = input(" -> ")

                client_socket.send(message.encode())



if __name__ == '__main__':
    client_program()