# Kamus sandi Morse dalam bahasa Indonesia
morse_code = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '/': ' '
}

def morse_to_text(morse):
    morse_words = morse.split(' / ')
    translated_text = ''
    for word in morse_words:
        letters = word.split(' ')
        translated_word = ''
        for letter in letters:
            if letter in morse_code:
                translated_word += morse_code[letter]
        translated_text += translated_word + ' '
    return translated_text.strip()

def text_to_morse(text):
    translated_morse = ''
    for char in text:
        char = char.upper()
        if char in morse_code.values():
            for key, value in morse_code.items():
                if value == char:
                    translated_morse += key + ' '
                    break
        elif char == ' ':
            translated_morse += '/ '
    return translated_morse.strip()

# Fungsi untuk meminta input dari pengguna
def get_user_input():
    print("Selamat datang di aplikasi Terjemahan Sandi Morse!")
    print("1. Terjemahkan Sandi Morse ke Teks")
    print("2. Terjemahkan Teks ke Sandi Morse")
    choice = input("Silakan pilih opsi (1/2): ")
    if choice == '1':
        morse = input("Masukkan sandi Morse: ")
        translated_text = morse_to_text(morse)
        print("Hasil terjemahan: ", translated_text)
    elif choice == '2':
        text = input("Masukkan teks: ")
        translated_morse = text_to_morse(text)
        print("Hasil terjemahan: ", translated_morse)
    else:
        print("Opsi yang dimasukkan tidak valid. Silakan coba lagi.")

# Menjalankan aplikasi
get_user_input()
