class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        maxheap=[-f for f in freq.values()] #negative because there is no builtin maxheap that orders values from maximum to minimum in python
        heapq.heapify(maxheap) #orders values in descending order --> assume lowest negative number is the highest frequency
        time=0
        q=deque()
        while maxheap or q:
            time+=1
            if maxheap:
                f = 1 + heapq.heappop(maxheap)
                if f:
                    q.append([f,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time


        