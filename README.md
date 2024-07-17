# Sistem Pengenalan Wajah untuk Pelanggan Supermarket

## Deskripsi Proyek
Proyek ini bertujuan untuk mengembangkan sistem pengenalan wajah yang dapat mengidentifikasi pelanggan supermarket berdasarkan dataset wajah yang dikumpulkan. Setiap wajah yang dikenali akan dihubungkan ke basis data SQLite yang menyimpan profil pelanggan, termasuk informasi seperti nama, jenis kelamin, usia perkiraan, riwayat pembelian, dan rekomendasi produk.

## Langkah-langkah Implementasi

### 1. Pengumpulan DataPengumpulan Data  
- Gunakan skrip /pengambilan.py untuk mengambil data wajah dari setidaknya 5 pelanggan supermarket. Saya menggunakan file “haarcascade_frontalface_default.xml” yang tersedia pada link https://github.com/opencv/opencv/tree/master/data/haarcascades untuk mendapatkan skrip pengkelasan wajah yang telah disediakan oleh OpenCV.
- Siapkan 5 gambar wajah pelanggan.
- Pastikan setiap gambar wajah sudah terdokumentasi dengan baik dan diberi label yang sesuai dengan profil pelanggan.
- Contoh hasil data wajah akan tersimpan di direktori /DataSet.
- Pastikan data tersebut mencakup variasi yang mencukupi dalam jenis kelamin, usia, dan kondisi cahaya.

### 2. Integrasi Basis Data SQLite
- Buat basis data SQLite dengan struktur tabel yang mencakup kolom-kolom seperti nama, jenis kelamin, tanggal kunjungan terakhir, usia, riwayat pembelian (3 produk teratas), dan rekomendasi produk berikutnya.

### 3. Pelatihan Model Pengenalan Wajah
- Pilih model pengenalan wajah yang sesuai, misalnya OpenCV FaceRecognizer atau model dari dlib.
- Latih model menggunakan dataset wajah yang telah dikumpulkan.
- Dokumentasikan proses pelatihan, termasuk hiperparameter yang dipilih dan evaluasi performa model.

### 4. Evaluasi Model
- Evaluasi kinerja model menggunakan metrik seperti akurasi, presisi, recall, dan skor F1.
- Gunakan dataset pengujian untuk menguji kemampuan model dalam mengenali wajah pelanggan.

### 5. Implementasi Sistem
- Implementasikan sistem pengenalan wajah yang dapat berjalan secara real-time menggunakan kamera atau video.
- Hubungkan sistem pengenalan wajah ke basis data SQLite untuk memperbarui profil pelanggan.

### 6. Dokumentasi
- Kompilasi laporan proyek yang mencakup semua temuan, kode, dan hasil evaluasi.
- Sertakan penjelasan detail setiap langkah, dari pengumpulan data hingga integrasi sistem.

## Struktur Repositori
- **/dataset**: Direktori untuk menyimpan dataset wajah pelanggan.
- **/models**: Direktori untuk menyimpan model yang telah dilatih.
- **/src**: Direktori untuk kode sumber aplikasi pengenalan wajah.
- **/docs**: Direktori untuk dokumen-dokumen proyek, termasuk laporan proyek dan dokumentasi teknis.

