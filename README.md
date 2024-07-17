# Sistem Pengenalan Wajah untuk Pelanggan Supermarket

## Deskripsi Proyek
Proyek ini bertujuan untuk mengembangkan sistem pengenalan wajah yang dapat mengidentifikasi pelanggan supermarket berdasarkan dataset wajah yang dikumpulkan. Setiap wajah yang dikenali akan dihubungkan ke basis data SQLite yang menyimpan profil pelanggan, termasuk informasi seperti nama, jenis kelamin, usia perkiraan, riwayat pembelian, dan rekomendasi produk.

## Langkah-langkah Implementasi

### 1. Pengumpulan DataPengumpulan Data  
- Gunakan skrip **/pengambilan.py** untuk mengambil data wajah dari setidaknya 5 pelanggan supermarket.
- Gunakan file “haarcascade_frontalface_default.xml” yang tersedia pada link https://github.com/opencv/opencv/tree/master/data/haarcascades untuk mendapatkan skrip pengkelasan wajah yang telah disediakan oleh OpenCV.
- Siapkan 5 gambar wajah pelanggan.
- Pastikan setiap gambar wajah sudah terdokumentasi dengan baik dan diberi label yang sesuai dengan profil pelanggan.
- Contoh hasil data wajah akan tersimpan di direktori **/DataSet**.
- Pastikan data tersebut mencakup variasi yang mencukupi dalam jenis kelamin, usia, dan kondisi cahaya.

### 2. Integrasi Basis Data SQLite
- Buat basis data SQLite dengan nama **/store.db** menggunakan langkah seperti pada link https://medium.com/@986110101/pengenalan-wajah-5-cb65f3726e44.
- Buat dengan struktur tabel yang mencakup kolom-kolom seperti nama, jenis kelamin, tanggal kunjungan terakhir, usia, riwayat pembelian (3 produk teratas), dan rekomendasi produk berikutnya.

### 3. Pelatihan Model Pengenalan Wajah
- Pilih model pengenalan wajah yang sesuai, misalnya OpenCV FaceRecognizer atau model dari dlib.
- Latih model menggunakan dataset wajah yang telah dikumpulkan menggunakan skrip **/pelatihan**.

### 4. Evaluasi Model
- Evaluasi kinerja model menggunakan metrik seperti akurasi, presisi, recall, dan skor F1 menggunakan skrip **/evaluasi**.
- Gunakan dataset pengujian untuk menguji kemampuan model dalam mengenali wajah pelanggan.

### 5. Implementasi Sistem
- Implementasikan sistem pengenalan wajah yang dapat berjalan secara real-time menggunakan kamera atau video.
- Hubungkan sistem pengenalan wajah ke basis data SQLite untuk memperbarui profil pelanggan.
- Gunakan skrip **/hasil_deteksi**.

### 6. Dokumentasi
- Pengumpulan DataPengumpulan Data
![Screenshot 2024-07-17 212018](https://github.com/user-attachments/assets/7f480b8f-ad2d-45a7-9e4a-280730ae455d)
- Integrasi Basis Data SQLite
![Screenshot 2024-07-17 214337](https://github.com/user-attachments/assets/977e17ee-582b-43bf-985d-4d0d627ab145)
- Pelatihan Model Pengenalan Wajah dan Evaluasi Model
![Screenshot 2024-07-17 214537](https://github.com/user-attachments/assets/f7e66628-ce7b-4ab7-9ace-1d28e250d0aa)
- Implementasi Sistem
![Screenshot 2024-07-17 214826](https://github.com/user-attachments/assets/667adf5f-e457-4cdb-8931-57cc4b7bd3e7)
.png…]()


## Struktur Repositori
- **/dataset**: Direktori untuk menyimpan dataset wajah pelanggan.
- **/models**: Direktori untuk menyimpan model yang telah dilatih.
- **/src**: Direktori untuk kode sumber aplikasi pengenalan wajah.
- **/docs**: Direktori untuk dokumen-dokumen proyek, termasuk laporan proyek dan dokumentasi teknis.

