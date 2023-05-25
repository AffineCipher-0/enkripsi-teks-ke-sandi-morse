# Membuat kamus sandi Morse
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': '/'
}

# Fungsi untuk mengenkripsi teks menjadi sandi Morse
def encrypt_morse(text):
    encrypted_text = ''
    for char in text:
        char = char.upper()
        if char in morse_code:
            encrypted_text += morse_code[char] + ' '
    return encrypted_text

# Contoh penggunaan
plaintext = "Terlalu banyak makan bakso membuat badan menjadi gemuk"
encrypted_text = encrypt_morse(plaintext)
print("Plaintext: ", plaintext)
print("Encrypted Text (Morse Code): ", encrypted_text)
