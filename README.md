# Otakudesu Scraper - Python Project

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Scraping](https://img.shields.io/badge/purpose-web%20scraping-yellowgreen)

Sebuah web scraper untuk situs Otakudesu (situs anime Indonesia) yang ditulis dalam Python. Scraper ini dapat mengambil berbagai informasi anime dari situs Otakudesu secara otomatis.

## Fitur Utama
- 📺 Scraping daftar anime terbaru
- 🔥 Scraping daftar anime populer
- ℹ️ Scraping detail anime lengkap (judul, genre, rating, sinopsis, dll)
- 📥 Scraping daftar episode dan link download
- 🔍 Pencarian anime berdasarkan judul
- 🎨 Tampilan berwarna di terminal (colorama)
- 🧩 Struktur kode modular dan mudah dikembangkan

## Prasyarat
Sebelum menjalankan program ini, pastikan Anda telah menginstal:
- Python 3.6+
- pip (Python package manager)

## Instalasi
1. Clone repository ini:
```bash
git clone https://github.com/lexaiko/otakudesu-scraper.git
cd otakudesu-scraper
```

2. Instal dependensi yang dibutuhkan:
```bash
pip install -r requirements.txt
```

### Dependensi Utama
| Package | Version | Kegunaan |
|---------|---------|----------|
| requests | latest | Untuk melakukan HTTP requests |
| beautifulsoup4 | latest | Untuk parsing HTML |
| lxml | latest | HTML parser |
| colorama | latest | Untuk tampilan berwarna di terminal |

## Penggunaan
Jalankan program utama dengan perintah:
```bash
python otakudesu.py
```

### Menu Interaktif
Setelah menjalankan program, Anda akan melihat menu berikut:
```
=== Otakudesu Scraper ===
1. Cari Anime
2. Anime On Going
3. Anime Full

Pilih opsi [1-4]: 
```

### Contoh Penggunaan Lengkap
1. **Melihat anime terbaru**:
   - Pilih opsi 1
   - Program akan menampilkan daftar anime terbaru:
   ```
   Daftar Anime Terbaru:
   [1] Jujutsu Kaisen 2nd Season
       URL: https://otakudesu.wiki/anime/jujutsu-kaisen-2nd-season-sub-indo/
   [2] Mushoku Tensei II: Isekai Ittara Honki Dasu
       URL: https://otakudesu.wiki/anime/mushoku-tensei-ii-sub-indo/
   ...
   ```

2. **Melihat anime populer**:
   - Pilih opsi 2
   - Program akan menampilkan daftar anime populer:
   ```
   Daftar Anime Populer:
   [1] One Piece
   [2] Attack on Titan: The Final Season
   [3] Demon Slayer: Kimetsu no Yaiba
   ...
   ```

3. **Mencari anime**:
   - Pilih opsi 3
   - Masukkan judul anime (contoh: "demon slayer")
   - Program akan menampilkan hasil pencarian:
   ```
   Hasil Pencarian untuk "demon slayer":
   [1] Demon Slayer: Kimetsu no Yaiba
   [2] Demon Slayer: Kimetsu no Yaiba Movie - Mugen Train
   [3] Demon Slayer: Kimetsu no Yaiba - Entertainment District Arc
   ...
   ```
   - Pilih nomor anime untuk melihat detail lengkap

### Contoh Output Detail Anime
```markdown
Judul: Demon Slayer: Kimetsu no Yaiba
Japanese: 鬼滅の刃
Rating: 8.6
Status: Completed
Tayang: Spring 2019
Studio: ufotable
Genre: Action, Demons, Historical, Shounen, Supernatural
Jumlah Episode: 26

Sinopsis:
Di era Taisho Jepang, Tanjiro Kamado adalah anak laki-laki yang baik hati yang menjadi 
penjual arang untuk menghidupi keluarganya. Suatu hari, seluruh keluarganya dibantai 
oleh iblis, kecuali adik perempuannya Nezuko yang berubah menjadi iblis. Untuk 
mengembalikan Nezuko menjadi manusia dan membalas dendam pembunuh keluarganya, 
Tanjiro menjadi pembasmi iblis.

Daftar Episode:
1. Episode 1: Cruelty - https://otakudesu.wiki/episode/demon-slayer-ep-1/
2. Episode 2: Trainer Sakonji Urokodaki - https://otakudesu.wiki/episode/demon-slayer-ep-2/
...
26. Episode 26: New Mission - https://otakudesu.wiki/episode/demon-slayer-ep-26/

Link Download:
[480p] https://download.link/480p
[720p] https://download.link/720p
[1080p] https://download.link/1080p
```

## Struktur Kode
```plaintext
otakudesu-scraper/
├── otakudesu.py           # Program utama
├── scraper.py             # Modul utama untuk scraping
├── utils.py               # Fungsi utilitas
├── requirements.txt       # Daftar dependensi
├── LICENSE
└── README.md
```

## Berkontribusi
Kontribusi selalu diterima! Berikut cara berkontribusi:
1. Fork project ini
2. Buat branch fitur baru (`git checkout -b fitur-baru`)
3. Commit perubahan Anda (`git commit -am 'Menambahkan fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request baru

### Fitur yang Dapat Ditambahkan
- [ ] Scraping anime berdasarkan musim
- [ ] Scraping anime berdasarkan genre
- [ ] Dukungan untuk download episode langsung
- [ ] Export hasil ke format JSON/CSV
- [ ] GUI versi sederhana

## Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](LICENSE) untuk detailnya.

## Catatan Penting
1. Scraper ini dibuat untuk tujuan edukasi dan penggunaan pribadi
2. Gunakan dengan bijak dan bertanggung jawab
3. Situs Otakudesu mungkin mengubah struktur HTML mereka sewaktu-waktu yang dapat menyebabkan scraper berhenti bekerja
4. Jika terjadi error, silakan buka issue di GitHub
5. Dukung situs resmi dengan menonton anime melalui platform legal

## Troubleshooting
**Error: Module tidak ditemukan**
Pastikan semua dependensi terinstal:
```bash
pip install -r requirements.txt
```

**Error: Scraping gagal**
1. Cek koneksi internet Anda
2. Cek apakah struktur situs Otakudesu telah berubah
3. Coba jalankan ulang program

**Program tidak menampilkan warna:**
Pastikan terminal Anda mendukung ANSI color codes

---
Dibuat dengan ❤️ oleh [lexaiko](https://github.com/lexaiko) | Jika terbantu, jangan lupa kasih ⭐!
