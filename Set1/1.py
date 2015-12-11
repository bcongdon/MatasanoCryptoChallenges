import base64
import binascii

def hex_to_base64(string):
	return str(base64.b64encode(binascii.a2b_hex(string)))

challange = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
print hex_to_base64(challange) == expected
