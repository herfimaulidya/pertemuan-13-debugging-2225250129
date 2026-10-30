# Pertemuan 13 — Debugging, Tracing, Testing, dan Test Case

## 1. Kasus

Praktik ini membahas proses debugging pada program pengolahan nilai mahasiswa. Program memiliki tiga fungsi utama:

- `hitung_rata_rata()`: menghitung rata-rata nilai.
- `status()`: menentukan status kelulusan mahasiswa.
- `nilai_tertinggi()`: mencari nilai tertinggi.

Data yang digunakan:

```python
nilai = [80, 60, 90, 70]
```

## 2. Identifikasi Bug

Ditemukan tiga bug pada program awal:

| Kode | Bug | Penyebab |
|---|---|---|
| B01 | Hasil rata-rata tidak tepat | Pembagi ditetapkan menjadi 5, padahal jumlah data 4 |
| B02 | Nilai 60 dinyatakan tidak lulus | Menggunakan operator `>` sehingga nilai 60 tidak memenuhi kondisi |
| B03 | Nilai tertinggi menghasilkan 0 | Inisialisasi dan operator perbandingan tidak tepat |

## 3. Perbaikan Bug

Perbaikan yang dilakukan:

1. Mengganti pembagi tetap dengan `len(nilai)`.
2. Mengganti operator `>` menjadi `>=` pada fungsi status.
3. Menginisialisasi nilai tertinggi menggunakan `nilai[0]` dan membandingkan dengan operator `>`.

## 4. Test Case

| Test | Input | Hasil yang Diharapkan |
|---|---|---|
| T1 | `[80, 60, 90, 70]` untuk rata-rata | 75.0 |
| T2 | `[100, 80]` untuk rata-rata | 90.0 |
| T3 | `60` untuk status | Lulus |
| T4 | `59` untuk status | Tidak lulus |
| T5 | `[80, 60, 90, 70]` untuk nilai tertinggi | 90 |

## 5. Hasil Retest

Seluruh lima test case berhasil dijalankan dan menghasilkan output sesuai harapan.

```text
T1 - Rata-rata: 75.0
T2 - Rata-rata: 90.0
T3 - Status 60: Lulus
T4 - Status 59: Tidak lulus
T5 - Nilai tertinggi: 90
```

## 6. Cara Menjalankan Program

Jalankan perintah berikut melalui terminal:

```bash
py praktik/praktik_4_debugging.py
```

Untuk menjalankan test case:

```bash
py latihan/03_test_case.py
```

## 7. Refleksi

Melalui praktik ini, saya mempelajari cara menemukan dan memperbaiki kesalahan pada program menggunakan debugging dan tracing. Saya juga memahami pentingnya membuat test case untuk memastikan program berjalan sesuai dengan hasil yang diharapkan. Selain itu, penggunaan Git membantu mendokumentasikan perubahan kode sebelum dan sesudah perbaikan.