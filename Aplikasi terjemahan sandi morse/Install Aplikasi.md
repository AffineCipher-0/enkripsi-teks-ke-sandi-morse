python -m PyInstaller --noconsole --onefile fileperccobaan.py

Untuk menerjemahkan sandi Morse ke teks:

1. Input sandi Morse dibagi menjadi kata-kata dengan memisahkan berdasarkan tanda "/ ".
	- Setiap kata kemudian dibagi menjadi huruf-huruf dengan memisahkan berdasarkan spasi (" ").
	- Setiap huruf sandi Morse diterjemahkan ke dalam teks berdasarkan kamus morse_code.
	- Setiap huruf yang berhasil diterjemahkan ditambahkan ke dalam string hasil terjemahan.
	- Setelah semua huruf selesai diterjemahkan, kata tersebut ditambahkan ke dalam string hasil terjemahan.
	- Hasil terjemahan sandi Morse ke teks kemudian dikembalikan.
	- Untuk menerjemahkan teks ke sandi Morse:

2. Setiap karakter teks diubah menjadi huruf besar.
	- Jika karakter tersebut ada dalam kamus morse_code (huruf), maka sandi Morse yang sesuai diambil dari kamus.
	- Jika karakter tersebut adalah spasi, maka ditambahkan tanda "/ " sebagai pemisah antara kata.
	- Hasil terjemahan teks ke sandi Morse kemudian dikembalikan.


algoritma pemrosesan string

Untuk lebih jelasnya bagaimana program bekerja

Untuk menerjemahkan sandi Morse ke teks:

1. Sandi Morse dipecah menjadi kata-kata dengan menggunakan fungsi split(' / '). Ini akan memisahkan setiap kata yang dipisahkan oleh tanda "/ ".
	- Setiap kata dipecah menjadi huruf-huruf dengan menggunakan fungsi split(' '). Ini akan memisahkan setiap huruf yang dipisahkan oleh spasi.
	- Untuk setiap huruf dalam kata, dilakukan pencocokan dengan kamus morse_code menggunakan pernyataan if untuk mencari terjemahan huruf tersebut.
	- Huruf yang berhasil ditemukan dalam kamus morse_code ditambahkan ke dalam string translated_word.
	- Setelah selesai mencari terjemahan untuk setiap huruf dalam kata, translated_word ditambahkan ke dalam string translated_text dengan spasi sebagai pemisah.
	- Setelah selesai menerjemahkan setiap kata, string translated_text yang berisi teks hasil terjemahan sandi Morse dikembalikan.

2. Untuk menerjemahkan teks ke sandi Morse:
	- Setiap karakter dalam teks diubah menjadi huruf besar menggunakan fungsi upper() untuk memastikan pencocokan dengan kamus morse_code.
	- Untuk setiap karakter dalam teks, dilakukan pencocokan dengan kamus morse_code menggunakan pernyataan if untuk mencari terjemahan karakter tersebut.
	- Jika karakter ditemukan dalam kamus morse_code, sandi Morse yang sesuai ditambahkan ke dalam string translated_morse.
	- Jika karakter adalah spasi, tanda "/ " ditambahkan ke dalam string translated_morse sebagai pemisah antara kata.
	- Setelah selesai menerjemahkan setiap karakter dalam teks, string translated_morse yang berisi sandi Morse hasil terjemahan dikembalikan.

	Algoritma yang digunakan lebih mirip dengan pemetaan satu-ke-satu antara karakter sandi Morse dan karakter teks yang sesuai, berdasarkan kamus morse_code.