import string
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--file_path", required=True, type=str, help="Path to text file"
    )
    parser.add_argument("-k", "--key", required=True, type=int)
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


def encode_code(text: str, key: int) -> str:
    alfabet = string.ascii_lowercase
    power_alphabet = len(alfabet)

    result = ""

    for symbol in text:
        try:
            index = alfabet.index(symbol)
        except ValueError:
            index = -1

        if index < 0:
            result += symbol
        else:
            code_index = (power_alphabet + index + key) % power_alphabet
            result += alfabet[code_index]

    return result


def read_file(file_path: str) -> str:
    with open(file_path, "r") as read_file:
        return read_file.read()


def write_file(file_name: str, text: str) -> None:
    with open(file_name, "w") as write_file:
        write_file.write(text)


def main():
    args = parse_args()
    text = read_file(args.file_path)

    if args.mode == 0:
        key = int(args.key)
    else:
        key = -int(args.key)

    result = encode_code(text, key)

    output_file = "output.txt"
    write_file(output_file, result)


if __name__ == "__main__":
    main()
