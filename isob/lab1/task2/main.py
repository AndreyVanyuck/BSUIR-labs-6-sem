import argparse
from string import ascii_lowercase


def read_file(file_path: str) -> str:
    with open(file_path, "r") as read_file:
        return read_file.read()


def write_file(file_name: str, text: str) -> None:
    with open(file_name, "w") as write_file:
        write_file.write(text)


def generate_key(key: str, len_text: int) -> str:
    new_key = list(key)
    while len(new_key) < len_text:
        new_key.extend(key)
    return "".join(new_key)[: len_text + 1]


def define_alphabet(letter: str) -> tuple:
    ENG_ALPH = ascii_lowercase
    RUS_ALPH = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    if letter in ENG_ALPH or letter in RUS_ALPH:
        curr_alph = ENG_ALPH if letter in ENG_ALPH else RUS_ALPH
        return (curr_alph, len(curr_alph))
    else:
        return (None, None)


def vigenere_code(text: str, key: str, mode: int) -> str:
    cipher_text = []
    i = 0
    for letter in text:
        alph, power_alph = define_alphabet(letter.lower())
        if alph is None:
            cipher_text.append(letter)
            continue
        kv = alph.find(key[i].lower())
        if mode:
            index = (alph.find(letter.lower()) - kv + power_alph) % power_alph
        else:
            index = (alph.find(letter.lower()) + kv) % power_alph
        ciph_let = alph[index]
        cipher_text.append(ciph_let if letter.islower() else ciph_let.upper())
        i += 1
    return "".join(cipher_text)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file_path", required=True, type=str, help="path to text file"
    )
    parser.add_argument("-k", "--key", required=True, type=str)
    parser.add_argument(
        "-m",
        "--mode",
        required=True,
        type=int,
        choices=[0, 1],
        default=0,
        help="mode: 0 - encrypt, 1 - decrypt",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    
    text = read_file(args.file_path)
    key = generate_key(args.key, len(text))
    mode = args.mode

    result = vigenere_code(text, key, mode)

    output_file = "output.txt"
    write_file(output_file, result)


if __name__ == "__main__":
    main()