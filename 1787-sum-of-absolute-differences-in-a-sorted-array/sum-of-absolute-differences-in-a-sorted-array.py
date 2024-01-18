class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum=0
        total_sum=sum(nums)
        result=[]

        for i,n in enumerate(nums):
            rightsum=total_sum-left_sum-n
            left_size=i
            right_size=len(nums)-i-1
            result.append(
                left_size*n-left_sum +   rightsum  - right_size*n 
                )

            left_sum+=n

        return result




        