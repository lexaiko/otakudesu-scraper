# Otakudesu Scraper - Python Project

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Scraping](https://img.shields.io/badge/purpose-web%20scraping-yellowgreen)

Scraper untuk situs Otakudesu (situs anime Indonesia) yang ditulis dalam Python. Scraper ini dapat mengambil berbagai informasi anime dari situs Otakudesu secara otomatis.

## Fitur Utama
- 🔍 Pencarian anime berdasarkan judul
- 📺 Daftar anime on-going (berkelanjutan)
- 📚 Daftar semua anime yang tersedia
- 📥 Daftar episode dan link embed player
- ℹ️ Detail informasi anime (genre, status, rating)

## Prasyarat
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

## Cara Penggunaan
Jalankan program utama dengan perintah:
```bash
python otakudesu.py
```

### Menu Utama
```
Pilih opsi:
1. Search Anime
2. Lihat Anime On Going
3. Lihat Semua List Anime
Masukkan pilihan (1/2/3): 
```

### Alur Kerja Program
1. **Pencarian Anime**:
   - Pilih opsi 1 dan masukkan judul anime
   - Program menampilkan hasil pencarian
   - Pilih anime untuk melihat daftar episode

2. **Anime On Going**:
   - Pilih opsi 2
   - Program menampilkan anime yang sedang berlanjut
   - Pilih anime untuk melihat daftar episode

3. **Semua List Anime**:
   - Pilih opsi 3
   - Program menampilkan semua anime yang tersedia
   - Pilih anime untuk melihat daftar episode

4. **Lihat Episode**:
   - Setelah memilih anime, program menampilkan daftar episode
   - Pilih episode untuk mendapatkan link embed player

### Contoh Output
```
Pilih opsi:
1. Search Anime
2. Lihat Anime On Going
3. Lihat Semua List Anime
Masukkan pilihan (1/2/3): 1

Masukkan judul anime: demon slayer
[SEARCHING] demon slayer...

Ditemukan hasil:

1. Demon Slayer: Kimetsu no Yaiba — https://otakudesu.cloud/anime/demon-slayer-kimetsu-no-yaiba/
2. Demon Slayer Movie — https://otakudesu.cloud/anime/demon-slayer-movie/
3. Demon Slayer: Entertainment District Arc — https://otakudesu.cloud/anime/demon-slayer-entertainment-district-arc/

Pilih nomor anime untuk lihat episode: 1

[DETAIL] Demon Slayer: Kimetsu no Yaiba

1. Episode 1 — https://otakudesu.cloud/episode/demon-slayer-ep-1/
2. Episode 2 — https://otakudesu.cloud/episode/demon-slayer-ep-2/
...
26. Episode 26 — https://otakudesu.cloud/episode/demon-slayer-ep-26/

Pilih nomor episode untuk ambil semua embed link: 1

🎬 Embed link yang ditemukan:
https://example.com/embed/12345
https://example.com/embed/67890
```

## Dependencies
Package yang digunakan:
- `requests` : Untuk melakukan HTTP requests
- `beautifulsoup4` : Untuk parsing HTML
- `lxml` : HTML parser

## Troubleshooting
**Error: Module tidak ditemukan**
```bash
pip install requests beautifulsoup4 lxml
```

**Error: Scraping gagal**
1. Cek koneksi internet
2. Cek apakah situs Otakudesu masih bisa diakses
3. Struktur website mungkin telah berubah

**Hasil tidak ditemukan**
- Gunakan keyword pencarian yang berbeda
- Pastikan anime tersedia di Otakudesu

## Catatan Penting
1. Scraper ini dibuat untuk tujuan edukasi
2. Gunakan dengan bijak dan bertanggung jawab
3. Struktur website dapat berubah sewaktu-waktu
4. Dukung situs resmi dengan menonton anime melalui platform legal

---
Dibuat dengan ❤️ oleh [lexaiko](https://github.com/lexaiko) | ⭐ Star repository ini jika bermanfaat!
