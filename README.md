# Caesar Cipher Encryption and Decryption

This Python script provides a command-line interface for encrypting and decrypting text using a simple substitution cipher. It takes in a shift value and either a text or a file as input and produces the corresponding encrypted or decrypted text.

## Prerequisites

- Python 3.x
- Required Python packages: `argparse`, `termcolor`, `unidecode`

Install the required packages using the following command:
```
pip install -r requirements.txt
```

## Usage

Run the script using the following command:
```
python3 caesar.py [-e] [-d] [-s SHIFT] [-t TEXT] [-f FILE]
```

### Options

- `-e` or `--encrypt`: Encryption mode.
- `-d` or `--decrypt`: Decryption mode.
- `-s SHIFT` or `--shift SHIFT`: Number of shifts for encryption or decryption (default is 3).
- `-t TEXT` or `--text TEXT`: Text to encrypt or decrypt. Specify the text in quotes if it contains spaces.
- `-f FILE` or `--file FILE`: File containing the text to encrypt or decrypt.

**Note:** You must specify either the encryption mode (`-e`) or the decryption mode (`-d`). Additionally, you must provide either the text (`-t`) or the file (`-f`) to encrypt or decrypt.

### Examples

Encrypting a text:
```
python3 caesar.py -e -t "A text"
```

Decrypting a text:
```
python3 caesar.py -d -t "D whaw"
```

Encrypting the content of a file:
```
python3 caesar.py -e -f input.txt
```

Decrypting the content of a file:
```
python3 caesar.py -d -f input.txt
```

## Acknowledgements

- The script utilizes the `argparse` library to handle command-line arguments.
- It uses the `termcolor` library to print colored output.
- The `unidecode` library is used to remove diacritics from characters.

## License

This project is licensed under the [MIT License](LICENSE).
