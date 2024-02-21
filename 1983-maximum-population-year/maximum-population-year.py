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















        # pop = [0] * 2051
        # res = 0
        # for l in logs:
        #     pop[l[0]] += 1
        #     pop[l[1]] -= 1
        
        # for i in range(1950, 2050):
        #     pop[i] += pop[i-1]
        #     if pop[i] > pop[res]:
        #         res = i
        
        # return res
        