# -*- coding: utf-8 -*-
"""
Takes rsa variables from user and encrypts
string provided through a command line argument

@author: jmcau
"""

import sys

"""
    encrypts of decrypts ascii chars 
    provide e for exp to encrypt
    provide d for exp to decrypt
"""
def encode(ascii_chars, exp, n):
    for i in range(len(ascii_chars)):
        ascii_chars[i] = ascii_chars[i] ** exp % n
    
    return ascii_chars
        
def ascii_values_to_string(ascii_chars):
    chars = []
    
    for i in range(len(ascii_chars)):
        chars.append(chr(ascii_chars[i]))
        
    return "".join(chars)

def string_to_ascii_values(s):
    chars = list(s)
    for i in range(len(chars)):
        chars[i] = ord(chars[i])
    
    return chars

def print_usage():
    print("Usage: py rsa.py <string to be encrypted>")
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)
        
    s = sys.argv[1]
    e = 0;
    d = 0;
    n = 0;
    
    try:
        e = int(input("e: "))
        d = int(input("d: "))
        n = int(input("n: "))
    except ValueError:
        print("Error: make sure you're entering numbers")
    
    """
        n must be large enough to cover the ascii table
    """    
    if n < 128:
        print("Error: n must be 128 or greater")
        sys.exit(1)
    
    """
        encode and decode the string provided by user
    """    
    
    print("Plaintext: " + s)
    
    chars = string_to_ascii_values(s)
    
    print("ASCII Plaintext: " + str(chars))
    
    chars = encode(chars, e, n)
    
    print("c = m ^ e is applied to each character")
    print("Encrypted ASCII: " + str(chars))
    
    print("Encrypted String: " + ascii_values_to_string(chars))
    
    print("m = c ^ d is applied to each character")
    chars = encode(chars, d, n)
    
    print("Decrypted ASCII: " + str(chars))
    
    print("Decrypted String: " + ascii_values_to_string(chars))
    
    
    
    