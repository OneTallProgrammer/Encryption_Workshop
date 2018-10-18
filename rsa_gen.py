# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import sqrt
import sys

"""
    returns true if x is prime
    returns false is x is not prime or
    x <= 1
"""
def isprime(x):
    if x == 2 or x == 3:
        return True
    
    if x < 2:
        return False
    
    if x % 2 == 0:
        return False
    
    for div in range(3, int(sqrt(x)) + 3, 2):
        if x % div == 0:
            return False
    
    return True
    

if __name__ == "__main__":
    p = 0
    q = 0
    e = 0
    d = 0
    n = 0
    r = 0
    
    """
        choose prime numbers p & q such that p and q 
        are positive and greater than 0
    """
    print("Enter prime numbers p and q")
    not_valid = True
    while(not_valid):
        try:
            p = int(input("p: "))
            q = int(input("q: "))
            if isprime(p) and isprime(q):
                not_valid = False
            else:
                print("Error: p and q must be prime")
        except ValueError:
            print("Error: Please make sure you enter a number")
            
    
    if p < 1 or q < 1:
        print("Error: Please enter a positive number")
        sys.exit()
    
    """
        get n by multiplying p and q
        get r by multiplying (p - 1) and (q - 1)
    """
    n = p * q
    r = (p - 1)*(q - 1)
    
    print("n = p * q = " + str(p * q))
    print("r = (p-1) * (q-1) = " + str((p - 1) * (q - 1)))
    
    """
        select e such that 1 < e < r and gcd(e, r) 
        is 1
        This means that e is a prime number that 
        does not divide evenly into r
    """
    
    print("Select e such that 1 < e < r and r is not divisible by e")
    not_valid = True
    while not_valid:
        
        while not_valid:
            try:
                e = int(input("e: "))
                if isprime(e):
                    not_valid = False
                else:
                    print("Error: " + str(e) + " is not prime")
                    continue
                
            except ValueError:
                print("Error: Please make sure you enter a number")
                continue
            
        if e < 1 or e >= r:
            print("Error: Please e must be a positive number less than r")
            not_valid = True
            continue
        
        if r % e == 0:
            print("Error: Make sure e does not divide into r")
            not_valid = True
        
    """
        calculate d such that d * e mod r = 1
    """
    print("Select d such that 1 < d < r and e * d % r = 1")
    print("Algorithm selects r (it's a little annoying)")
    for x in range(r):
        if e * x % r == 1:
            d = x
    
    print("::: Your Encryption Values Are :::")
    print("p: " + str(p))
    print("q: " + str(q))
    print("n: " + str(n))
    print("r: " + str(r))
    print("e: " + str(e))
    print("d: " + str(d))
    print("::: Use c = m^e to encrypt :::")
    print("::: Use m = c^d to decrypt :::")
    print("::: Note: c must be less than n :::")