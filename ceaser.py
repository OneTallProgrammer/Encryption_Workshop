# -*- coding: utf-8 -*-
"""
A basic ceaser cipher 

@author: jmcau
"""

import sys

begin = 97
end = 122

"""
    Move all characters in s down the alphabet by the shift amount
"""

def ceasar(shift, s):
    global begin
    global end
    
    chars = list(s)
    
    for i in range(len(chars)):
        new_char = ord(chars[i])
        new_char += shift
    
        # make sure the characters are in the alphabet
        while(new_char < begin):
            new_char += end - begin + 1
        while(new_char > end):
            new_char -= end - begin + 1
    
        chars[i] = chr(new_char)
        
    return "".join(chars)

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
    print("Usage: py ceaser.py <shift> <string>")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print_usage()
        sys.exit()
    
    """
    ascii limits
    """
    shift = 0
    
    try:
        shift = int(sys.argv[1])
    except ValueError:
        print("Error: shift must be an integer")
        
    s = sys.argv[2]
    s = clean_string(s)
    print("Plaintext: " + s)
    
    s = ceasar(shift, s)
    print("Ciphertext: " + s)
    
    
    
    
    