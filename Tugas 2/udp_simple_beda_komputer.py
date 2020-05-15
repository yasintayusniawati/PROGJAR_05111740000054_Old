import socket

TARGET_IP = "10.151.253.138"
TARGET_PORT = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes('Yasinta-ProgjarC'.encode()),(TARGET_IP,TARGET_PORT))