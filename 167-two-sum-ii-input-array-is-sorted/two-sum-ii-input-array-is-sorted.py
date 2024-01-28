class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j and i<len(numbers) and j<(len(numbers)):
            summ=numbers[i]+numbers[j]
            if summ==target:
                return [i+1,j+1]
            if summ>target:
                j-=1
            elif summ<target:
                i+=1
        