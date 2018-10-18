# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:27:50 2018

@author: jmcau
"""

import sys

begin = 97 # a
end = 122  # z

def rotate_by_keysize_and_position(string, start, keysize, offset):
    global begin
    global end
    
    chars = list(string)
    
    for i in range(start, len(chars), keysize):
        if chars[i] == '.':
            continue
        
        ascii_val = ord(chars[i])
        ascii_val -= offset
        
        while(ascii_val < begin):
            ascii_val += end - begin + 1
        while(ascii_val > end):
            ascii_val -= end - begin + 1
            
        chars[i] = chr(ascii_val)
        
    return "".join(chars)

def remove_chars(string, start, keysize):
    chars = list(string)
    
    for i in range(start, len(chars), keysize):
        chars[i] = '.'
    
    return "".join(chars)
            

"""
    ensure that all character in s are in the alphabet
"""
def invalid_string(s):
    global begin
    global end
    
    chars = list(s)
    
    for char in chars:
        if ord(char) > end or ord(char) < begin:
            return True
    
    return False
    

def print_usage():
    print("Used for rotating every nth character where n is the keysize")
    print("starting with the specified character")
    print("Usage: py rotator.py <string>")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
        sys.exit()
    
    string = sys.argv[1]
    
    if invalid_string(string):
        print("Error: string can only contain characters from the alphabet")
        sys.exit()
    
    start = 0
    keysize = 1
    
    not_valid = True
    while not_valid:
        try:
            start = int(input("Enter starting character: "))
            if(start >= 1):
                not_valid = False
            else:
                print("Error: start must be greater than 0")
        except ValueError:
            print("Error: start must be an integer")
            
    not_valid = True
    while not_valid:
        try:
            keysize = int(input("Enter keysize: "))
            if(keysize >= 1):
                not_valid = False
            else:
                print("Error: keysize can't be less than 1")
        except ValueError:
            print("Error: keysize must be an integer")
            
    """
    specify characters positions to be removed
    """
    print("Would you like to remove characters?")
    print("Specify what index you would like to start at or 0 to quit")
    print("Characters will be removed based on keysize")
    not_valid = True
    removals = []
    while not_valid:
        try:
            removals.append(int(input("Remove characters starting at: ")))
            if removals[-1] < 0:
                print("Error: can't be a negative number")
                removals.pop()
            elif removals[-1] == 0:
                not_valid = False
                removals.pop()
            
        except ValueError:
            print("Error: removal starting index must be an integer")
    
    for removal in removals:
        string = remove_chars(string, removal - 1, keysize)
    
    for offset in range(end - begin + 1):
        output = rotate_by_keysize_and_position(string, start - 1, keysize, offset)
        print(str(chr(offset + begin)) + ": " + output)
        
        
       
       
       