import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 31002

# Bind the socket to the port
server_address = ('10.151.253.199', port)
print(f"starting up on {server_address} port {port}")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("Menunggu koneksi dari client")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    
    NamaFile = 'gambar1_sever_'+str(port)+'.png'
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
    FileTerima.close()
    connection.close()