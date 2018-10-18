# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:29:38 2018

@author: jmcau
"""

import sys

begin = 97  # a
end = 122   # z

"""
    checks keyword for illegal characters
"""
def validate_key(key):
    global begin
    global end
    
    key = key.lower()
    chars = list(key)
    for char in chars:
        if(ord(char) > end or ord(char) < begin):
            return False
    
    return True

def encode(key, plain, decrypting):
    global begin
    global end
    
    key_ch = list(key)
    plain_ch = list(plain)
    
    key_i = 0
    
    for i in range(len(plain_ch)):
        ascii_val = ord(plain_ch[i])
        shift = ord(key_ch[key_i]) - begin
        
        if decrypting:
            ascii_val -= shift
        else:
            ascii_val += shift
        
        while(ascii_val < begin):
            ascii_val += end - begin + 1
        while(ascii_val > end):
            ascii_val -= end - begin + 1
            
        new_char = chr(ascii_val)
        plain_ch[i] = new_char
        
        key_i += 1
        if key_i >= len(key_ch):
            key_i = 0
            
    return "".join(plain_ch)

"""
    all upper case characters are lowered
    eliminates whitespace
    eliminates all characters outside of alphabet
"""
def clean_string(s):
    global begin
    global end
    
    chars = list(s.lower())
    
    while ' ' in chars:
        chars.remove(' ')
    
    for char in chars:
        if ord(char) < begin or ord(char) > end:
            chars.remove(char)
    
    return "".join(chars)

def print_usage():
    print("Usage: py ceaser.py <-d or -e> <keyword> <string>")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print_usage()
        sys.exit()
    
    opt = sys.argv[1]
    decrypting = False
    if opt == "-d":
        decrypting = True
    elif opt != "-e":
        print("Error: please specify whether you are encrypting or decrypting")
        sys.exit()
        
    
    """
    save password
    """
    key = sys.argv[2]
        
    input_str = sys.argv[3]
    input_str = clean_string(input_str)
    print("Plaintext: " + input_str)
    
    output = encode(key, input_str, decrypting)
    print("Ciphertext: " + output)