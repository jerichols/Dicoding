## Pertanyaan Bisnis
- Bagaimana pengaruh waktu (hr) terhadap jumlah penggunaan sepeda casual pada rental bike?
- Bagaimana pengaruh hari libur (holiday) terhadap jumlah penggunaan sepeda pada rental bike?

## Cleaning Data

Pada tahap cleaning data saya mengubah value dari kolom - kolom yang menggunakan angka. Hal ini saya lakukan dikarenakan agar Data Frame Tersebut lebih mudah untuk dibaca.

Di tahap ini saya menggunakan :
```
replace()
```
Untuk mengubah ke value yang saya inginkan.

## Exploratory Data Analysis
### Pertanyaan 1
 Disini saya menggabungkan variable 'hr' dengan 'casual' yang bernama 'hour_per_casual' untuk mencari pengaruh waktu terhadap pengguna casual menggunakan sysntax : 
```
groupby()
```

### Pertanyaan 2
Disini saya menggabungkan variable 'holiday' dengan 'cnt' yang bernama 'usage_by_holiday' untuk mencari pengaruh hari libur terhadap pengguna sepeda dengan hari libur.
Saya menggunakan syntax yang sama pada pertanyaan 1.
Lalu saya mencari korelasi antara kedua variable tersebut menggunakan : 
```
corr()
```

## Visualization & Explanatory Analysis
### Pertanyaan 1 
Pada pertanyaan ini saya menggunakan bar chart untuk mengetahui pada waktu jam berapa pengunjung casual paling banyak. Saya menggunakan bar chart dikarenakan saya dapat melihat lonjakan serta puncak dari jam tersebut.

### Pertanyaan 2
Pada pertanyaan ini saya menggunakan bar char juga karena saya ingin membandingkan 2 kategori holiday dan melihat mana yang paling banyak.
