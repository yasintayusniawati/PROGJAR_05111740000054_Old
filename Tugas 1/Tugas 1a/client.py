import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)


try:
    NamaFile = "gambar1.png"
    FileKirim = open(NamaFile, 'rb')
    for data in FileKirim:
        sock.sendall(data)
    print('Berhasil dikirim')

finally:
    print("closing")
    sock.close()