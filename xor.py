# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:39:46 2018

@author: jmcau
"""

import sys

"""
    encodes the bytes of a file using XOR encryption
    @param byts: the bytearray containing the file data
    @param key: the string password used for encryption
    @return: encoded bytearray
"""
def encode(byts, key):
    key_i = 0
    key = list(key)    

    for i in range(len(byts)):
        byts[i] = byts[i] ^ ord(key[key_i])
        key_i += 1
        
        if key_i == len(key):
            key_i = 0
            
    return byts

def print_usage():
    print("Encrypts a file using XOR encryption")
    print("I accept no responsibility if you try to encode sensitive data" +
          " and something goes wrong")
    print("FOR ENTERTAINMENT USE ONLY!!!")
    print("Usage: py xor.py <key> <message>")

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print_usage()
        sys.exit()
    
    key = sys.argv[1]
    file_path = sys.argv[2]
    
    # read in the characters in the file and interpret them as binary
    byts = bytearray(open(file_path, 'rb').read())
    
    # perform XOR encryption on the file
    byts = encode(byts, key)
    
    # overwrite the contents of the file with the ciphertext
    with open(file_path + ".copy", 'wb') as f:
        f.write(byts)
