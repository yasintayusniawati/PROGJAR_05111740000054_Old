import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('10.151.252.189', 31000)
print(f"starting up on {server_address}")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("Menunggu koneksi dari client")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    
    NamaFile = 'gambar2_sever.png'
    FileTerima = open(NamaFile, 'wb+')

    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(64)
        if data:
            FileTerima.write(data)
        else:
            print(f"file diterima dari {client_address}")
            break
    # Clean up the connection
    connection.close()