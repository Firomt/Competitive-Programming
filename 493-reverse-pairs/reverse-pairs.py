class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums,low,mid,high):
            temp=[]
            left=low
            right=mid+1
            while left<=mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1
            while left <= mid:
                temp.append(nums[left])
                left+=1
            while right<=high:
                temp.append(nums[right])
                right+=1
            for i in range(low, high + 1):
                nums[i] = temp[i - low]
        
        def mergesort(nums,low,high):
            cnt = 0
            if low >= high:
                return cnt
            mid = (low + high)//2
            cnt += mergesort(nums,low,mid)
            cnt += mergesort(nums,mid+1,high)
            cnt += countpairs(nums,low,mid,high)
            merge(nums,low,mid,high)
            return cnt

        def countpairs(nums,low,mid,high):
            cnt=0
            right=mid+1
            for i in range(low,mid+1):
                while right <= high and nums[i]>2*nums[right]:
                    right+=1
                cnt +=right-(mid+1)
            return cnt



        return mergesort(nums,0,len(nums)-1)
        


            
                    
                
            
    


        