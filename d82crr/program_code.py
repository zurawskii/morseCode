import tkinter.messagebox
from tkinter import Canvas, Label

import tkinter as tk

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

screen = tkinter.Tk()

encoded = Label(screen, text='', font=('Helvetica 20 bold'), fg='black', padx=5, pady=10)


def encode():
    text = inputField.get().upper()
    print(text)
    encodeCode = ""
    for letter in text:
        if letter in MORSE_CODE_DICT:
            if len(encodeCode) != 0:
                if encodeCode[len(encodeCode)-1] == " ":
                    pass
                else:
                    encodeCode += " "
            encodeCode += MORSE_CODE_DICT[letter]
        else:
            if letter == ' ':
                print("here")
                encodeCode += ' / '

    print(encodeCode)
    encoded.config(text=encodeCode)
    encoded.grid(column=0, row=4, columnspan=4, pady=10)
    return encodeCode


decoded = Label(text='', font=('Helvetica 20 bold'), fg='black', padx=5, pady=10)


def decode():
    decodeCode = ""
    new_text = encode().replace(' / ', '/')
    new_text = encode().split(' ')
    print("New text: ", new_text)
    for el in new_text:
        if el == '/':
            decodeCode += " "
        for key, value in MORSE_CODE_DICT.items():
            if value == str(el):
                decodeCode += key

    print(decodeCode)
    decoded.config(text=decodeCode)
    decoded.grid(column=0, row=5, columnspan=4, pady=10)
    return decodeCode


screen.title("Encoding and Decoding Morse Code Program")
screen.config(width=1200, height=1200, padx=250, pady=250, bg="#2b2d42")

inputField = tk.Entry(screen, width=100)
inputField.grid(column=0, row=2, ipady=7, pady=20, columnspan=3)
inputField.focus()

buttonEncode = tk.Button(screen, text="ENCODE", width=30, bg="#ef233c", pady=6, border=0, font=('Helvetica 12 bold'),
                         command=encode)
buttonEncode.grid(column=1, row=3, padx=25, pady=15)

buttonDecode = tk.Button(screen, text="DECODE", width=30, bg="#8d99ae", pady=6, border=0, font=('Helvetica 12 bold'),
                         command=decode)
buttonDecode.grid(column=2, row=3, padx=25, pady=15)

canvas = Canvas(screen, width=500, height=150, bg="#d90429", highlightthickness=False)
canvas.create_text(250, 75, text="Encoding and Decoding\nMorse Code Program", fill="#edf2f4",
                   font=('Helvetica 24 bold'), justify='center')
canvas.grid(column=0, row=1, columnspan=3, pady=25)


screen.mainloop()
