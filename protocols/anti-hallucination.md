# Anti-Halusinasi

## Inventaris klaim

Untuk setiap klaim, catat:

- teks atau ringkasan klaim;
- sumber `file:heading`, `file:page`, atau `brief`;
- tipe: fakta, angka, opini, kutipan, sebab-akibat, prediksi, atau fiksi;
- tingkat kepastian;
- status: `VERIFIED`, `SOURCE-RELATIVE`, `UNVERIFIED`, atau `CONFLICT`.

## Batas penciptaan

Boleh menyusun ulang, meringkas, menghubungkan, dan membuat transisi. Tidak boleh menambah nama, angka, tanggal, sumber, kutipan, studi, contoh faktual, atau latar belakang yang tidak diberikan.

Untuk fiksi, detail baru boleh dibuat hanya bila brief mengizinkan penciptaan. Detail itu harus konsisten dengan canon proyek dan dicatat sebagai keputusan kreatif, bukan fakta sumber.

## Flag

Jika sumber meragukan, jangan memperbaiki diam-diam. Tulis:

```text
⚠️ Flag: [klaim] — status [UNVERIFIED/CONFLICT]. Verifikasi atau ubah sebelum publikasi.
```

## Gate

- Semua klaim sumber punya pasangan di output.
- Tidak ada klaim output tanpa sumber atau keputusan kreatif.
- Negasi, angka, nama, kutipan, kausalitas, dan tingkat kepastian tetap.
- Placeholder tidak boleh tertinggal tanpa dilaporkan.
