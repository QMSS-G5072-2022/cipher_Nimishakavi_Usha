## importing necessary libraries

def cipher_ukn2102(text, shift, encrypt=True):
	'''
	A function to encrypt or decrypts a string based on shift value
	3 attributes: a string, an integer to shift the string, and a boolean True to encrypt or False to decrypt
	example of encryption:
		text = today
		shift = 1
		encrypt = True
			returns upebz
	example of decryption:
		text = upebz
		shift = 1
		encrypt = False
			returns -> today
	'''
	alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	new_text = ''
	for c in text:
		index = alphabet.find(c)
		if index == -1:
			new_text += c
		else:
			new_index = index + shift if encrypt == True else index - shift
			new_index %= len(alphabet)
			new_text += alphabet[new_index:new_index+1]
		return new_text