def cipher_ukn2102(text, shift, encrypt=True):
	"""
	Encrypt or decrypts a string based on shift value

	Parameters
	-----------
	text    : a string
	shift   : an integer to shift the string, 
	encrypt : a boolean True to encrypt or False to decrypt

	Returns
	--------
	Encrypted or decrypted text string

	Examples
	--------
	>>> cipher_ukn2102(text = 'today', shift = 1, encrypt = True)
	'upebz'
	>>> cipher_ukn2102(text = 'upebz', shift = 1, encrypt = False)
	'today'
	"""
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