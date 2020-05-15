from socket import *
import socket
import threading
import logging
import time
import sys

from person_machine import PersonMachine

pm = PersonMachine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        while True:
            """ Membaca command yang didapat"""
            header = b''
            while True:
                data = self.connection.recv(1)
                if data.decode() == '\n':
                    break
                header += data
            print(header)
            """============================="""
            if header:
                d = header.decode()
                hasil = pm.proses(d,self.connection)
                hasil=hasil+"\r\n"
                self.connection.sendall(hasil.encode())
            else:
                break
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 8889))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()

