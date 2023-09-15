morze = {'a': '.-', 'b': '-…', 'c': '-.-.', 'd': '-..',
         'e': '.', 'f': '..-.', 'g': '--.', 'h': '….',
         'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
         'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
         'q': '--.-', 'r': '.-.', 's': '…', 't': '-',
         'u': '..-', 'v': '…-', 'w': '.--', 'x': '-..-',
         'y': '-.--', 'z': '--..'}


def word_to_morze(word: str):
    for letter in word:
        try:
            print(morze[letter], end='')
        except KeyError:
            print(f'UNEXPECTED letter: {letter}')
    print()


def text_to_morze(text: str):
    for word in text.split(' '):
        word_to_morze(word)


def clear_text(text: str):
    return text.lower().replace('\n', ' ').replace('\t', ' ')


def main():
    text_to_morze(clear_text(input()))


if __name__ == "__main__":
    main()
