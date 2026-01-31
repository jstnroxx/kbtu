# Bitwise operators are used to compare (binary) numbers.
"""
&   	AND	Sets each bit to 1 if both bits are 1	    x & y	
|   	OR	Sets each bit to 1 if one of two bits is 1  	x | y	
^	    XOR	Sets each bit to 1 if only one of two bits is 1 	x ^ y	
~   	NOT	Inverts all the bits    	~x	
<<	    Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off    	x << 2	
>>	    Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off 	x >> 2
"""

# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0.
print(6 & 3)
# The binary representation of 6 is 0110.
# The binary representation of 3 is 0011.
# Then the & operator compares the bits and returns 0010, which is 2 in decimal.

# The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0.
print(6 | 3)
# The binary representation of 6 is 0110.
# The binary representation of 3 is 0011.
# Then the | operator compares the bits and returns 0111, which is 7 in decimal.

# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0.
print(6 ^ 3)
# The binary representation of 6 is 0110.
# The binary representation of 3 is 0011.
# Then the ^ operator compares the bits and returns 0101, which is 5 in decimal.