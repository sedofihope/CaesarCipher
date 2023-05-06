#!/usr/bin/env python3
#encoding:utf-8

import os
import argparse
from termcolor import cprint
from unidecode import unidecode

def cipherEncrytpion(text, n, letters):
	encrypted = ''
	for l in unidecode(text.upper()):
		if l in letters:
			x = (letters.index(l)+n)%26
			encrypted += letters[x]
		else:
			encrypted += l

	return encrypted

def cipherDecrytpion(text, n, letters):
	decrypted = ''
	for l in unidecode(text.upper()):
		if l in letters:
			x = (letters.index(l)-n)%26
			decrypted += letters[x]
		else:
			decrypted += l

	return decrypted

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-e', '--encrypt', action="store_true", dest="encrypt", help="Encryption mode")
	parser.add_argument('-d', '--decrypt', action="store_true", dest="decrypt", help="Decryption mode")
	parser.add_argument('-s', '--shift', action="store", dest="shift", type=int, default=3, help="Number of shifts (3 by default)")
	parser.add_argument('-t', '--text', action="store", dest="main_text", metavar='TEXT', help="Text to encrypt or decrypt", nargs='+', type=str)
	parser.add_argument('-f', '--file', action="store", type=argparse.FileType('r'), dest="filename", help="File containing the text to encrypt or decrypt")

	args = parser.parse_args()

	if not args.encrypt and not args.decrypt:
		cprint("[+] Specify encryption or decryption or check help.",'red', attrs=['bold'])
		cprint("[+] Example : cipher.py -e -t 'A text'",'yellow', attrs=['bold'])
		exit()
	else:
		if not args.main_text and not args.filename:
			cprint("[+] Specify a text or a file or check help.",'red', attrs=['bold'])
			cprint("[+] Example : cipher.py -e -t 'A text'",'yellow', attrs=['bold'])
			exit()
		else:
			if args.main_text:
				text = ' '.join(args.main_text)
			elif args.filename:
				text = args.filename.read()

			n = args.shift
			letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
						'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
						'W', 'X', 'Y', 'Z']

			if args.encrypt:
				cprint(cipherEncrytpion(text, n, letters), 'yellow')
				exit()
			elif args.decrypt:
				cprint(cipherDecrytpion(text, n, letters), 'yellow')
				exit()

if __name__ == '__main__':
	main()
