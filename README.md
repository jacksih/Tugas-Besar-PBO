# Tugas-Besar-PBO
Tugas Besar PBO kelompok 7 Kelas PBO-RC Yang berisikan:
1. Marchell Manurung (120140208)
2. Namira Aulia (120140210)
3. Shakira Fairuz Putri (120140217)
4. Dhilan Septa Yudha (120140224)
5. Jacky Z.M Sihombing (120140226)
6. Satrio Maruli Jaya Sianturi (120140238)
## :alien: Judul Proyek
Space Invaders
## :alien: Deskripsi Proyek
Space invaders adalah sebuah game arcade yang bertema di luar angkasa, yang terinspirasi oleh media lain: Breakout, The War of the Worlds, dan Star Wars. Space invaders adalah game tembak-menembak yang menampilkan grafik 2D. Tujuan dari game ini adalah untuk mendapatkan skor tertinggi dengan menembakan laser ke enemy. 
Aturan Permainan : 
- Player dapat menembakkan laser dan hanya dapat bergerak secara horizontal. 
- Enemy disejajarkan dalam formasi persegi, enemy dapat bergerak secara horizontal dan vertikal dan dapat menembakan laser ke arah player.
- Jika enemy ditembak oleh player dengan laser, maka enemy akan hancur/hilang.
- Jumlah awal nyawa (heart) adalah tiga.
- Terdapat tiga tipe enemy. setiap enemy yang tereleminasi masing-masing bernilai 100, 200, dan 300
- Kondisi Menang/Kalah, jika menang ketika semua enemy telah kalah/hilang, maka layar ucapan "selamat ! anda menang" akan ditampilkan atau jika kalah ketika semua     nyawa(heart) PLAYER telah HABIS, maka player kalah. 

## :alien: Dependensi paket (library) yang dibutuhkan untuk menjalankan aplikasi
Library python adalah kumpulan modul terkait berisi kumpulan kode yang dapat digunakan berulang kali dalam program yang berbeda. Adanya library membuat pemrograman python menjadi lebih sederhana dan nyaman bagi programmer karena tidak perlu menulis kode yang sama berulang kali untuk program yang berbeda. Pygame adalah modul cross-platform dari Python dirancang untuk membuat game. Modulnya dirancang untuk menjadi sederhana, mudah digunakan, dan menyenangkan. Modul sys adalah modul yang berfungsi untuk mengakses program itu sendiri dan menjalankan file kode python di lingkungan direktori atau sistem itu sendiri.
## :alien: Cara menjalankan aplikasi (cara bermain)
- Open File main.py yang berada di folder python (pastikan anda telah menginstall pygame pada aplikasi untuk menjalankan program)
- Kemudian setelahnya run program untuk dapat memainkan permainan
- Terdapat beberapa shortcut dalam permainan. Tombol Shortcut 1 untuk langsung memenangkan permainan dan Tombol Shortcut 2 dan player akan langsung kalah.
## :alien: UML class diagram proyek
![UML Class Diagram (4)](https://user-images.githubusercontent.com/77344442/170223193-b10cf73f-9bbf-447d-9ff9-4483f58d6b69.png)


## :alien: Cara menjalankan kontainer
Docker adalah teknologi containerisasi yang memungkinkan kita untuk membangun, menguji, dan menggunakan aplikasi dengan dimana saja yang berada dalam sebuah wadah disebut container. Konsep Docker mirip virtual machine.
1. Buatlah Docker file. Dockerfile merupakan sebuah file yang mana pada file tersebut berisikan berbagai macam instruksi yang akan dieksekusi untuk membangun sebuah image.
2. Buat juga Build Image, jalankan perintah docker build. Kita bisa memberikan tag dengan parameter --tag 
```bash
docker build --tag space-invaders
  ```
3. Setelah berhasil membuild imagenya, kemudian jalankan command di root terminal.
```bash
XAUTH=$HOME/.Xauthority
touch $XAUTH
xhost +
  ```
4. Kemudian run docker melalui command.
```bash
docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY --device /dev/snd space-invaders.
  ```

## :alien: Kontributor pengembangan aplikasi
1. Marchell Manurung (120140208)
2. Namira Aulia (120140210)
3. Shakira Fairuz Putri (120140217)
4. Dhilan Septa Yudha (120140224)
5. Jacky Z.M Sihombing (120140226)
6. Satrio Maruli Jaya Sianturi (120140238)
