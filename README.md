# Sistem Klasifikasi Sampah Menggunakan Raspberry Pi 4 dengan model DenseNet 201
![img](assets/waste-demo.jpg)

### Nama dan NIM Anggota Penyusun

## Penjelasan Proyek Akhir
Projek ini bertujuan untuk mengimplementasikan sebuah sistem yang dapat mengidentifikasi dan mengklasifikasikan jenis sampah dengan menggunakan _Edge Devices_ dan sebuah perangkat komputasi berupa Raspberry Pi 4.

### Tujuan Pengembangan Sistem
- Sampah masih menjadi masalah besar yang dihadapi hampir seluruh negara di dunia, termasuk Indonesia. Berdasarkan data dari Sistem Informasi Penanggulangan Sampah Nasional (SIPSN) pada tahun 2023, timbulan sampah di Indonesia mencapai 35,74 juta ton per tahun, meskipun jumlah ini sedikit menurun sebesar 7,47% dari tahun 2022.
- Sampah sering tidak dipilah dengan benar karena rendahnya kesadaran masyarakat dan keterbatasan infrastruktur. Selain itu, pemilahan manual kurang efisien dan akurat, sehingga diperlukan pendekatan teknologi yang lebih baik yaitu alat yang dapat mengidentifikasi dan klasifikasi sampah secara otomatis.
- Maka dari itu, di projek ini dibuat sebuah alat yang dapat mengidentifikasi dan mengklasifikasi sampah menggunakan algoritma dari CNN (Convolutional Neural Network) yagn berjudul DenseNet201 untuk mengidentifikasi dan mengklasifikasi empat jenis sampah yaitu, Anorganik, Organik, B3, dan Residu.

### Rumusan Masalah Proyek
- Berapa jumlah nilai _accuracy_ yang didapatkan oleh model DenseNet201?
- Bagaimana hasil _Confusion Matrix_ model DenseNet201?
- Bagaimana Hasil akurasi inferensi pada sistem identifikasi sampah?

## Implementasi Proyek
Pada bagian ini, akan disusun mengenai rekayasa dari perangkat lunak dan perangkat keras yang digunakan pada proyek untuk membangun sistem guna mengidentifikasi dan mengklasifikasikan jenis sampah.

### Diagram Keseluruhan Sistem
![img](assets/system-flowchart.png)

### Rekayasa Perangkat Keras
- **Raspberry Pi 4 Model B Ram 4 GB**: _Single Board Computer_ yang digunakan sebagai perangkat komputasi utama dalam sistem.
- **Logitech Webcam C270**: Perangkat yang digunakan untuk mengambil citra dari sampah yang akan diklasifikasi.
- **Servo SG90 180**: Perangkat yang digunakan untuk menggerakan katup pada tempat sampah.

### Datasheet Raspberry Pi 4 Model B
![img](assets/raspi-datasheet.jpg)

### Diagram Skematik Sistem
![img](assets/system-schematic.png)

## Proses Demo dan Evaluasi Sistem
- **Persiapan**: Proses untuk menghubungkan setiap komponen yang digunakan dalam sistem dan mengunggah kode program ke dalam perangkat komputasi Raspberry Pi 4 Model B.
- **Demonstrasi**: Melakukan demonstrasi alat untuk mengidentifikasi dan mengklasifikasikan jenis sampah yang dideteksi pada kamera
- **Evaluasi**: Melakukan proses pengujian di menggunakan jenis sampah yang berbeda-beda.

### Hasil Akhir Sistem
![img](assets/alat-1.jpg)
![img](assets/alat-2.jpg)
![img](assets/alat-3.jpg)

### Demo Pengimplementasian Sistem
