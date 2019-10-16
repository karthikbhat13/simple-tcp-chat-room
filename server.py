import select
import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


addr = '0.0.0.0'
port = 7777

recv_buf = 4096


def send_message(sock, message):
    print("message rec : ", message)
    m_dict = json.loads(message)
    addr = m_dict["addr"]
    mes = m_dict["text"]

    print(addr, mes)
    #
    # print(con_list)
    # recv_sock = con_list[addr]
    # print(recv_sock)
    # recv_sock.send(mes)

    print(con_list)
    for soc in con_list:
        if soc != server_socket and soc != sock:
            try:
                print("trying to send ", mes)
                print(soc)
                soc.send(mes.encode())
            except Exception as e:
                print("Exception!", e)
                soc.close()
                con_list.remove(soc)


if __name__ == "__main__":
    server_socket.bind((addr, port))

    server_socket.listen(10)

    con_list = [server_socket]

    users = []
    print("Chat server started : " + str(server_socket))

    while 1:
        read_sockets, write_sockets, error_sockets = select.select(con_list, [], [])

        for sock in read_sockets:
            if sock == server_socket:
                new_socket, new_addr = server_socket.accept()
                con_list.append(new_socket)

                print("new client ", new_addr)

            else:
                try:
                    client_data = sock.recv(recv_buf)

                    if client_data:
                        send_message(sock, client_data.decode("utf-8"))
                except:
                    sock.close()
                    con_list.remove(sock)

                    continue
    server_socket.close()