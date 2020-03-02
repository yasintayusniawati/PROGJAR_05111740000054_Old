import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('10.151.252.189', 32000)
print(f"starting up on {server_address}")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("Menunggu koneksi dari client")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")

    TerimaNama = connection.recv(64)
    NamaFile = TerimaNama.decode()

    try:
        FileKirim = open(NamaFile, 'rb')
        for data in FileKirim:
            connection.sendall(data)
        FileKirim.close()
    except IOError:
        connection.sendall(b'')
        

    # Clean up the connection
    connection.close()