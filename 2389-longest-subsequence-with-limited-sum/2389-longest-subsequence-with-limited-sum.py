class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer=[]
        total=sum(nums)
        
        for i in queries:
            j=0
            count=0
            current_sum=0
            if i>=total:
                answer.append(len(nums))
                continue
            while j < len(nums) and  current_sum+nums[j]<=i:
                current_sum+=nums[j]
                count+=1
                j+=1
            answer.append(count)
        return answer

        