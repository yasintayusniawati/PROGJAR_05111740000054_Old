# Tugas 4
![1](https://github.com/yasintayusniawati/PROGJAR_05111740000054/blob/master/Tugas%204/img/soal.jpg)

## Penjelasan
* Gambar meletakkan_file.jpg : Menjalankan server_person.py dan client_kirim.py untuk mengirimkan file gambar bart.png. Setelah file gambar terkirim akan diletakkan pada folder server dengan nama file bart.png

* Gambar mengambil_file.jpg : Menjalankan server_person.py dan client_get.py untuk mengambil file gambar bart.png. Setelah file gambar berhasil di ambil nama file yang diterima client menjadi client_bart.png

* Gambar melihat_list_file.jpg : Menjalankan server_person.py dan client_list.py untuk melihat list file yang ada pada server. File yang ada dalam database program ini adalah file bart.png dan gambar1.png


### a. Ketentuan membaca Format
string terbagi menjadi 2 bagian, dipisahkan oleh spasi
```
COMMAND spasi PARAMETER spasi PARAMETER ...
```
b. Daftar Fitur
- create : meletakkan file
- list : melihat daftar file yang ada di server
- get : untuk mengambil file

c. Cara melakukan request dan respon yang di dapat

- Create 
  request : create
  parameter : nama_file
  response : berhasil mengupload -> ok
             gagal mengupload -> error

- list
request: list
  parameter: tidak ada
  response: daftar file yang ada di server

- get 
request: get 
  parameter: nama_file yang diinginkan
  response: berhasil mendownload -> file yang direquest, beserta string success
            gagal mendownload -> error
