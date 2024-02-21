class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int: 
        events = []

        for start, end in logs:
            events.append([start, 1])  
            events.append([end, -1]) 
        events.sort()

        cur_max=0
        maxx=0
        for i in events:
            cur_max += i[1]
            if cur_max > maxx:
                maxx=max(cur_max, maxx)
                year=i[0]
        return year
        