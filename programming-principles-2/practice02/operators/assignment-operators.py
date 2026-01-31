# Assignment operators are used to assign values to variables.
"""
=   	x = 5   	x = 5	
+=  	x += 3  	x = x + 3	
-=  	x -= 3  	x = x - 3	
*=  	x *= 3  	x = x * 3	
/=  	x /= 3  	x = x / 3	
%=  	x %= 3  	x = x % 3	
//= 	x //= 3 	x = x // 3	
**= 	x **= 3 	x = x ** 3	
&=  	x &= 3  	x = x & 3	
|=  	x |= 3  	x = x | 3	
^=  	x ^= 3  	x = x ^ 3	
>>= 	x >>= 3 	x = x >> 3	
<<= 	x <<= 3 	x = x << 3	
:=  	print(x := 3)   	x = 3
                            print(x)
"""

# The Walrus Operator (:=). The count variable is assigned in the if statement, and given the value 5.
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")