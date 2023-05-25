# Kamus sandi Morse 
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '/': ' '
}

# Fungsi untuk menerjemahkan sandi Morse
def morse_to_text(morse):
    morse_words = morse.split(' / ')
    translated_text = ''
    for word in morse_words:
        letters = word.split(' ')
        translated_word = ''
        for letter in letters:
            for key, value in morse_code.items():
                if letter == key:
                    translated_word += value
                    break
        translated_text += translated_word + ' '
    return translated_text.strip()

# Fungsi untuk menerjemahkan teks ke sandi Morse 
def text_to_morse(text):
    translated_morse = ''
    for char in text:
        char = char.upper()
        for key, value in morse_code.items():
            if value == char:
                translated_morse += key + ' '
                break
    return translated_morse.strip()

# Contoh penggunaan
morse = '.... . .-.. .-.. --- '  # Sandi Morse
translated_text = morse_to_text(morse)
print("Morse Code: ", morse)
print("Translated Text: ", translated_text)

plaintext = "Belajar"  # Teks biasa
translated_morse = text_to_morse(plaintext)
print("Plaintext: ", plaintext)
print("Translated Morse Code: ", translated_morse)
