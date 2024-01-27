class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=0
        i=0
        j=len(height)-1
        while i<j and i<len(height) and j<len(height):
            if height[i]==0:
                i+=1
            if height[j]==0:
                j-=1
            if height[i]<=height[j]:
                area=height[i]*(j-i)
                maxArea=max(maxArea,area)
                #if height[j-1]>=height[i]:
                i+=1

            else:
                area=height[j]*(j-i)
                maxArea=max(maxArea,area)
                #if height[j-1]>=height[i]:
                j-=1
            
        return maxArea


