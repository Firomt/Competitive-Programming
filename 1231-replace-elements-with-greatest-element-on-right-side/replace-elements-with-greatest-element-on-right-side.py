class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        i=n-1
        while i > -1:
            if i==n-1:
                Max=arr[i]
                arr[i]=-1
                i-=1
            else:
                cur_num=arr[i]
                arr[i]=Max
                Max=max(Max,cur_num)
                i-=1
        return arr
        
        

            
        