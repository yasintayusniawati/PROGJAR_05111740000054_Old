from person import Person
import json
import logging

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

- create : untuk meletakkan file
  request : create
  parameter : nama_file
  response : berhasil mengupload -> ok
             gagal mengupload -> error

- list : untuk melihat daftar file yang ada di server
  request: list
  parameter: tidak ada
  response: daftar file yang ada di server

- get : untuk mengambil file
  request: get 
  parameter: nama_file yang diinginkan
  response: berhasil mendownload -> file yang direquest, beserta string success
            gagal mendownload -> error

- jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = Person()

class PersonMachine:
    def proses(self,string_to_process,connection):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='create'):
                logging.warning("create")
                nama_file = cstring[1].strip()

                """Menerima ukuran file yang diupload"""
                ukuran_inbyte = connection.recv(4)
                ukuran_asli = int.from_bytes(ukuran_inbyte,byteorder='big')
                """=================================="""

                """Terima File nya"""
                ukuran_diterima = 0
                recv_data=b''
                while ukuran_diterima < ukuran_asli:
                  data = connection.recv(64)
                  if data:
                      recv_data+=data
                      ukuran_diterima+=len(data)
                  else:
                      print(f"file diterima dari {client_address}")
                      break
                p.create_data(nama_file,recv_data)
                """==============="""

                return "OK"
            elif (command=='list'):
                logging.warning("list")
                hasil = p.list_data()
                return json.dumps(hasil)
            elif (command=='get'):
                logging.warning("get")
                nama = cstring[1].strip()

                hasil = p.get_data(nama)
                if not hasil:
                    nol = 0
                    nol = nol.to_bytes(4,byteorder='big')
                    connection.send(nol)
                    return "File tidak ada"
                ukuran = len(hasil['byte_data'])
                ukuran_inbyte = ukuran.to_bytes(4,byteorder='big')
                connection.send(ukuran_inbyte)
                # print('sending'+hasil['nama_file'])
                connection.sendall(hasil['byte_data'])
                return "Terkirim"
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    pm = PersonMachine()
    # hasil = pm.proses("list")
    # print(hasil)
    # hasil = pm.proses("get vanbasten")
    # print(hasil)