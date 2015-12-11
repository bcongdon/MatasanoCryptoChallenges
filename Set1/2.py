import binascii

def xor(in1,in2):
	result = int(in1,16) ^ int(in2,16)
	return str(hex(result))[2:-1]

in1 = '1c0111001f010100061a024b53535009181c'
in2 = '686974207468652062756c6c277320657965'
out = '746865206b696420646f6e277420706c6179'
print xor(in1,in2) == out