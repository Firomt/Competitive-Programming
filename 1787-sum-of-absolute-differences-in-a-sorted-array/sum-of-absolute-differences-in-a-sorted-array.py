class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum=0
        total_sum=sum(nums)
        result=[]

        for i,n in enumerate(nums):
            rightsum=total_sum-left_sum-n
            result.append(
                n*i-left_sum +   rightsum  - (len(nums)-i-1)*n 
                )

            left_sum+=n

        return result




        