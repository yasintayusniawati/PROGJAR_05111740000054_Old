## Tugas 9

#### 1. Jalankan kedua model tersebut
   * Server_async_http.py di port 45000
   * Server_thread_http.py di port 46000
#### 2. Ujicobalah dengan apache benchmark untuk 1000 request dan konkurensi yang bervariasi
   * Jumlah Request     : 1000
   * Konkurensi         : 1,2,3,4
#### 3. Hasil ujicoba dengan apache benchmark
  * Server Async : port 45000
  ![1](https://github.com/yasintayusniawati/PROGJAR_05111740000054/blob/master/Tugas%209/Screenshot/async/hasil_test.JPG)
  
  * Server Thread : 46000
  ![2](https://github.com/yasintayusniawati/PROGJAR_05111740000054/blob/master/Tugas%209/Screenshot/thread/hasil_test.JPG)

#### 4. Kesimpulan
Hasil test dari performance test pada tabel di atas menunjukkan bahwa menggunakan asynchronous server alokasi memory dan cpu akan lebih efisien. Sedangkan jika menggunakan server thread bila semakin banyak client yang melakukan request semakin banyak CPU time yang dibutuhkan dan penggunaan memory juga meningkat.
