import sys


MORSE_DICT = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    " ": "/"
}


def main():
    """
    Converts the given string into Morse code.
    Only accepts alphanumeric characters and spaces.
    """
    args = sys.argv[1:]

    try:
        if len(args) != 1:
            raise AssertionError("the arguments are bad")

        input_text = args[0].upper()

        if any(c not in MORSE_DICT for c in input_text):
            raise AssertionError("the arguments are bad")

        morse_output = " ".join(MORSE_DICT[c] for c in input_text)
        print(morse_output)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
