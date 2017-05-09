# Huffman Compression

## Directions

The whole program is written in one file, huff.py. Run it in a console or command prompt:

    >>> python huff.py

You will be prompted to enter some file names:

    >>> Enter file name: 128M.txt
    >>> Enter file to print encoding:
    >>> Enter file to print encoded text:
    >>> Enter file to print original text:

Input the file to be compressed. The rest can be left blank. The default file names are code for the frequency and huffman encoding, encoded.bin for the compressed binary file, and origfile.txt for the decompressed file.

Files will be generated for the encoding/frequency, compressed data, and decompressed data. File name will be displayed in the console.

--------------------

The program does the following:

### Encoding

1. Reads the text file and counts the frequency of each character using a Counter.

2. The character and frequency are used to build a Huffman tree, from which the character encoding is taken.

3. The encoding information is printed to a file.

4. The text file is read through and a string of encoded bits is constructed.

5. The encoded bit string is padded and converted to bytes, with the first byte denoting the amount of padding added.

### Decoding

1. The encoding key is read from the file.

2. The encoded text is read through and padding is removed.

3. The encoded string is read bit by bit and matched to see if it corresponds to an encoded character.

4. The decoded text is printed to a file.

--------------------

Written in Python 2.7.