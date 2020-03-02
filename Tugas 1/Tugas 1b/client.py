import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.151.252.189', 32000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    NamaFile = input('masukkan nama file :')
    sock.sendall(NamaFile.encode())

    data = sock.recv(64)
    if data:
        FileTerima = open(NamaFile+'_client', 'wb+')
        FileTerima.write(data)
        # Receive the data in small chunks and retransmit it
        while True:
            data = sock.recv(64)
            if data:
                FileTerima.write(data)
            else:
                print(f"file diterima")
                break
    else:
        print('file tidak ditemukan!')

finally:
    print("closing")
    sock.close()