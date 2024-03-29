class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total > 0:
                    right-=1
                elif total < 0:
                    left+=1
                else:
                    triplet=[nums[i],nums[left],nums[right]]
                    ans.append(triplet)
                    while left < right and nums[left]==triplet[1]:
                        left+=1
                    while left < right and nums[right]==triplet[2]:
                        right-=1
        return ans


        

        