import socket
import select

def server_program():

    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()

    server_socket.bind((host, port))

    server_socket.listen(2)

    con_list = [server_socket]

    while con_list:
        read_sock, write_sock, err_sock = select.select(con_list, [], con_list)

        for sock in read_sock:

            if sock == server_socket:
                new_con, new_addr = server_socket.accept()

                print("Connection from: ", str(new_addr))

                con_list.append(new_con)

            else:
                data = sock.recv(1024).decode()
                if not data:
                    break

                print("from connected user: " + str(data))
                for s in con_list:
                    if s != server_socket and s != sock:
                        print(s)
                        s.send(data.encode())



if __name__ == '__main__':
    server_program()