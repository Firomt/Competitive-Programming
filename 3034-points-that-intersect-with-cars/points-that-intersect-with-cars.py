class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        #solved based on understanding of line sweep algorithm   link-> https://leetcode.com/discuss/study-guide/2166045/line-sweep-algorithms
        point_line=[0]*102
        for st,end in nums:
            point_line[st]+=1
            point_line[end+1]-=1
        
        points=0
        for i in range(1,101):
            point_line[i] += point_line[i-1]
            if point_line[i] != 0:
                points+=1
        return points
   