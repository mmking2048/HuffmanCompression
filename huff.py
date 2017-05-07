import codecs
from collections import *
from heapq import heappush, heappop, heapify
import time

""" encoding """

"""
get frequency of characters in file
"""
def freqs(file):
  with open(file) as f:
	  counter = Counter()
	  for line in f:
	    counter += Counter(line)
  return counter

"""
generate huffman encoding given frequency
input: list of symbols and frequencies
output: list of symbols and huffman encodings
"""
def encode(symb2freq):
  heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
  heapify(heap)
  while len(heap) > 1:
    lo = heappop(heap)
    hi = heappop(heap)
    for pair in lo[1:]:
      pair[1] = '0' + pair[1]
    for pair in hi[1:]:
      pair[1] = '1' + pair[1]
    heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
  return sorted(heappop(heap)[1:], key = lambda p: (len(p[-1]), p))
  
"""
generate encoded string
"""
def get_encoded_string(filename, huffdict):
  encoded = ""
  with open(file) as f:
	for line in f:
		for c in line:
			encoded += huffdict[c]
	return encoded
	
"""
pad string for bytes
"""
def pad_encoded_string(encoded):
  extra_padding = 8 - len(encoded) % 8
  for i in range(extra_padding):
    encoded += "0"
  return "{0:08b}".format(extra_padding) + encoded
  
"""
convert to bytearray
"""
def get_byte_array(padded):
  b = bytearray()
  for i in range(0, len(padded), 8):
    byte = padded[i : i + 8]
    b.append(int(byte, 2))
  return b
  
""" decoding """
"""
"""
def read_key(codefile):
  code = dict()
  with open(codefile) as f:
	  for line in f:
		  words = line.split('\t')
		  code[words[2].strip()] = codecs.decode(words[0].strip("'"), "unicode_escape")
  return code

"""
unpad string
"""
def remove_padding(padded):
  extra_padding = int(padded[: 8], 2)
  padded = padded[8 :]
  encoded = padded[: -1 * extra_padding]
  return encoded

"""
decode string according to saved huffman encoding
"""
def decode_string(encoded, key, textfile):
  with open(textfile, 'w') as output:
    word = ""
    decoded = ""
    for bit in encoded:
      word += bit
      if word in key:
        output.write(key[word])
        word = ""


# ask for file name
file = raw_input("Enter file name: ")
codefile = raw_input("Enter file to print encoding: ")
outfile = raw_input("Enter file to print encoded text: ")
textfile = raw_input("Enter file to print original text: ")
  
# preset file names
codefile = codefile if codefile else "code"
outfile = outfile if outfile else "encoded.bin"
textfile = textfile if textfile else "origfile.txt"
  
"""
Part 1: encode file
"""
# read in file and list frequency
print("Reading file")
t1 = time.time()
freq = freqs(file)
  
print("Read time: {0}".format(time.time() - t1))
t2 = time.time()
  	
# build huffman tree
print("Constructing Huffman tree")
huff = encode(freq)
huffdict = dict(huff)
  
print("Tree building time: {0}".format(time.time() - t2))
  
# print character, frequency, and code to a file
with open(codefile, 'w') as f:
	for p in huff:
	  # write to file
		f.write("%s\t%s\t%s\n" % (repr(p[0]), freq[p[0]], p[1]))
  
t3 = time.time()
  
# replace each character in file with associated code
encoded = get_encoded_string(file, huffdict)
b = get_byte_array(pad_encoded_string(encoded))
with open(outfile, 'wb') as output:
  output.write(bytes(b))
  
  
print("Encoding time: {0}".format(time.time() - t3))
print("Frequency and huffman encoding is written to {0}".format(codefile))
print("Encoded file is written to {0}".format(outfile))
  
print("Total encoding time: {0}".format(time.time() - t1))
  
"""
Part 2: decode file
"""
# read in characters and encodings into dict
print("Reading key")
t4 = time.time()
key = read_key(codefile)
  
print("Read time: {0}".format(time.time() - t4))
t5 = time.time()
      
# read in characters and write text file
print("Generating original file")
with open(outfile, 'rb') as file:
  bit_string = ""
  byte = file.read(1)
  while byte != "":
    byte = ord(byte)
    bits = bin(byte)[2 :].rjust(8, '0')
    bit_string += bits
    byte = file.read(1)
    
  encoded = remove_padding(bit_string)
  decode_string(encoded, key, textfile)
  
print("Decode time: {0}".format(time.time() - t5))
print("Decoded file is written to {0}".format(textfile))