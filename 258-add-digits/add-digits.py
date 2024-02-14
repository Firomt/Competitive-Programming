class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        num = num // 10 + num % 10 
        return self.addDigits(num)