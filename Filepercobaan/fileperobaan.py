import PySimpleGUI as sg

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

# Layout untuk GUI
layout = [
    [sg.Text('Masukkan sandi Morse atau teks:')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('Terjemahkan'), sg.Button('Keluar')],
    [sg.Text('Hasil:')],
    [sg.Output(size=(40, 10), key='-OUTPUT-')]
]

# Membuat window dengan layout
window = sg.Window('Terjemahan Sandi Morse', layout)

# Event loop untuk GUI
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Keluar':
        break
    elif event == 'Terjemahkan':
        input_text = values['-INPUT-']
        if input_text.startswith('.') or input_text.startswith('-'):
            translated_text = morse_to_text(input_text)
            print(translated_text)
        else:
            translated_morse = text_to_morse(input_text)
            print(translated_morse)

window.close()
