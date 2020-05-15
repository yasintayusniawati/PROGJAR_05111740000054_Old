import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 31002

# Connect the socket to the port where the server is listening
server_address = ('10.151.253.199', port)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    NamaFile = input('masukkan nama file :')
    sock.sendall(NamaFile.encode())

    data = sock.recv(64)
    nama_seluruh = NamaFile.split('.')
    if data:
        FileTerima = open(nama_seluruh[0]+"_client_"+str(port)+"."+nama_seluruh[1], 'wb+')
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