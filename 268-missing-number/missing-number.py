class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #cycle sort concept
        #for the numbers from range [0,n] after sorting the correct index for each number is nums[i] while i is the number itself
        n=len(nums) 
        i=0
        while i < n:
            if nums[i]==n:
                i+=1
                continue
            correct=nums[i] 
            if nums[i] !=  nums[correct]:
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i:
                return i  #after sorting the numbers if the number and the index are not equal that means the index is the missing number
        return n #if after sorting the numbers and their respective index are equal that means n is the missing number 
            
    

               
        

  
        