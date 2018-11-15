# test wed site: https://crccalc.com/

# use a byte to make a WORD
def makeWord(b):
	c = b << 24
	for _ in range(8):
		if c & 0x80000000 :
			c = (c << 1 & 0xFFFFFFFF) ^ 0x04c11db7
		else:
			c = c << 1 & 0xFFFFFFFF
	print(hex(c))
	return c

# default setting: CRC-32/MPEG-2
def crc32(data, init = 0xFFFFFFFF, xorout = 0x00):
	crc = init
	for i in range(len(data)):
		crc = (crc << 8 & 0xFFFFFFFF) ^ makeWord(((crc >> 24) ^ data[i]) & 0xFF);
	crc = crc ^ xorout
	print(hex(crc))
	return crc

crc32(b'123456789') # check: 0x0376E6E7
print()
data=b'HelloWorld'
crc32(data) # 0xD7F46CC0

