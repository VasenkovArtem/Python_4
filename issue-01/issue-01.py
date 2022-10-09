"""Morse Code Translator"""

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе
    Не обрабатывает строчные буквы: следующий код не сработает
    >>> encode('sos') #doctest: +SKIP
    >>> encode('WHY ARE YOU SO SAD?')
    '.-- .... -.--   .- .-. .   -.-- --- ..-   ... ---   ... .- -.. ..--..'
    >>> encode('SOS')
    '... --- ...'
    >>> encode('SAVE MY SOUL!')
    Traceback (most recent call last):
      ...
    KeyError: '!'
    >>> encode('HELLO, WORLD')
    Traceback (most recent call last):
      ...
    KeyError: ','
    >>> encode('CAT, GO OUT')
    Traceback (most recent call last):
      ...
    KeyError:   ','
    >>> encode('Without sugar, please')
    Traceback (most recent call last):
      ...
    KeyError: 'i'
    >>> encode('With sugar, definitely') #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
      ...
    KeyError: ','
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


if __name__ == '__main__':
    msg = 'HELLO WORLD'
    morse_msg = encode(msg)
    print(morse_msg)
    assert morse_msg == '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'
