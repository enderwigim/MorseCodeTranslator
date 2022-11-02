morse_alphabet = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    ' ': '/'
}

def codify():
    user_word = input("Write a word to translate to morse: ")
    #list_user_word = user_word.split(" ")
    new_morse_word = ""
    # for word in user_word.split(" "):
    for letter in user_word:
        new_morse_word += morse_alphabet[letter.lower()] + " "
            # if letter.lower() in morse_alphabet:
            #     new_morse_word += morse_alphabet[letter.lower()]
            #     new_morse_word += " "

    print(new_morse_word)
    return new_morse_word


def deco():
    user_phrase = input("Write your morse code here: ")
    phrase_splited = user_phrase.split(" ")
    un_morse = ""
    for letter in phrase_splited:
        for morse_letter in morse_alphabet:
            if letter == morse_alphabet[morse_letter]:
                un_morse += morse_letter
    print(un_morse)
    return un_morse


codify()
deco()
