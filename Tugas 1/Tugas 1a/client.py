import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 31002

# Connect the socket to the port where the server is listening
server_address = ('10.151.253.199', port)
print(f"connecting to {server_address} port {port}")
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