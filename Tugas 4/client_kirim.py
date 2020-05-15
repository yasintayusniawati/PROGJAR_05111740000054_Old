import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8889

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', port)
print(f"connecting to {server_address} port {port}")
sock.connect(server_address)

command = input()
try:
    s = command
    NamaFile = s.split(" ")
    NamaFile = NamaFile[1].strip()
    command+='\n'
    sock.sendall(command.encode())

    """kirim ukuran file"""
    ukuran = os.path.getsize(NamaFile)
    sock.send(ukuran.to_bytes(4,byteorder='big'))
    """================="""

    """Kirim file"""
    FileKirim = open(NamaFile, 'rb')
    for data in FileKirim:
        sock.sendall(data)
    FileKirim.close()
    """========="""
except:
    print('err')
finally:
    response = sock.recv(1024)
    print(response.decode())
    sock.close()