# **DEPLOY MODEL**

## Deskripsi Singkat <br>
Model ini akan menampilkan data yang digunakan untuk melakukan deployment menggunakan Machile Learning dengan model Regresi Linier. Model yang akan digunakan pada tahapan ini akan “Memprediksi Kasus Kesembuhan” dengan memperhatikan Total kasus yang bertipe data int

## INPUT MODEL <br>
Agar dapat memprediksi tingkat penyembuhan kasus covid-19, user diminta untuk melakukan input total kasus covid yang berada di sekitarnya. Langkah melakukan inputan:
-	Mengisi total kasus dengan angka yang bertipe data int pada kolom yang sudah disediakan 
-	Lalu menekan tombol prediksi sekarang
-	Kemudian akan keluar, “Tingkat kesembuhan kasus covid-19 menurut total kasusnya"

## Folder, file dan kegunaan <br>
-	index.html --> Berisi template website
-	app.py --> Berisi konfigurasi route untuk API
-	model.pkl --> Model Regresi Linier yang sudah di-training

## Akses melalui website <br>
-	Buka URL menggunakan browser yang dimiliki, dengan menggunakan link https://deploy-covid19.herokuapp.com/
-	Kemudian masukkan input data yang akan diprediksi
-	Kemudian akan diberikan hasil prediksi tingkat kesembuhan kasus covid-19 menurut input yang diberikan
