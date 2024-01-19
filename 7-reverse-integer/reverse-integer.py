class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        y = str(x)
        
        if y[0] == '-':
            # If negative, reverse the digits (excluding the sign) and add the negative sign
            z = '-' + y[:0:-1]
        else:
            # If positive, reverse the digits
            z = y[::-1]
        
        # Convert the reversed string back to an integer
        w = int(z)
        
        # Check if the reversed integer is within the 32-bit signed integer range
        if w > INT_MAX or w < INT_MIN:
            return 0
        
        return w
