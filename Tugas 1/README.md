# Tugas 1
### Modifikasilah program client.py dan server.py agar dapat mentransfer file dari client ke server (letakkan program modifikasi di direktori tugas1a)
- Buka file client.py ubah server_address sesuai dengan ip komputer kita dan port. Misal : server_address = ('10.151.252.189', 31000)
- Tulisankan nama file yang ingin dikirimkan ke server pada bagian NamaFile. Misal NamaFile = "gambar1.png"
- Pada contoh ini saya menggunakan pc yang sama, sehingga gambar sebelum file dikirim ke server adalah sebagai berikut :

![sebelum_file_gambar1_dikirimkan (di client)](https://user-images.githubusercontent.com/37019733/75686541-0334d080-5ccf-11ea-8e12-06701b256a06.JPG)

- Buka file server.py ubah server_address sesuai dengan ip komputer kita dan port. Misal : server_address = ('10.151.252.189', 31000)
- Ubah nama file yang diterima pada server agar menghindari duplikasi nama. Misal : NamaFile = 'gambar1_sever.png'
- Jalankan server.py kemudian client.py
- Berikut adalah gambar setelah file gambar1.png dikirimkan ke server :

![setelah_file_gambar1_dikirimkan(di server)](https://user-images.githubusercontent.com/37019733/75688165-97a03280-5cd1-11ea-8dd7-1dc9d574f9fb.JPG)

### Modifikasilah program server.py agar dapat mengirimkan mentransfer file yang di request oleh client (letakkan program modifikasi di direktori tugas1b)
