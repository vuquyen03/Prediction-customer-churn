def binToDec(cmd):
	dec = []
	for binary in cmd:
		dec_num = 0
		for i in range (0, len(binary)):
			if binary[i] == '1':
				dec_num += 2 ** i
		dec.append(dec_num)
	word = ""
	for v in dec:
		word += chr(v)
	print(word)
def hexToDec(cmd):
	dec = []
	for v in cmd:
		temp = int(v, 16)
		dec.append(temp)
	word = ""
	for v in dec:
		word += chr(v)
	print(word)
def octToChar(cmd):
	dec = []
	for v in cmd:
		temp = int(v, 8)
		dec.append(temp)
	word = ""
	for i in dec:
		word += chr(i)
	print(word)

type = input()
if type == 'binary':
	cmd = [str(binary[::-1]) for binary in input().split()]
	print(cmd)
	binToDec(cmd)
if type == 'hexa':
	string = input()
	cmd = []
	i = 0
	while(i<=len(string)-2):
		temp = string[i:i+2]
		cmd.append(temp)
		i += 2
	print(cmd)
	hexToDec(cmd)
if type == 'octal':
	cmd = input().split()
	print(cmd)
	octToChar(cmd)