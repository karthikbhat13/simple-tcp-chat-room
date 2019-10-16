import socket
import sys
import json

def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()

def send_message(msg):
    addr_no, text = msg.split(',')
    json_dic = {}
    json_dic["addr"] = addr_no
    json_dic["text"] = text

    json_str = json.dumps(json_dic)

    s.send(json_str.encode())



if __name__ == "__main__":

    host = 'localhost'
    port = 7777

    recv_buf = 4096

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(20)

    # connect to remote host
    try:
        s.connect((host, port))
    except:
        print('Unable to connect')
        sys.exit()

    print("Client started")
    prompt()

    while 1:
        socket_list = [sys.stdin, s]

        read_sockets, write_sockets, error_sockets = [socket_list, [], []]

        for sock in read_sockets:
            if sock == s:

                data = sock.recv(recv_buf)

                if not data:
                    sys.exit()

                else:
                    sys.stdout.write(data)
                    prompt()

            else:
                msg = sys.stdin.readline()
                send_message(msg)
                prompt()