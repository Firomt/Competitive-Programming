class Solution:
    def addDigits(self, num: int) -> int:
 # Base case: If the number is a single digit, return it.
        if num < 10:
            return num 
        
        # Recursive case: Sum the digits of the number.
        # Example: 38 --> 3 + 8 --> 11
        num = num // 10 + num % 10 
        
        # Recursively call the function with the updated number.
        return self.addDigits(num)