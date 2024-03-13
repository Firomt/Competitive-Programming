class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()
        for i in range(1,n+1):
            queue.append(i)   
        while len(queue) > 1:
            for i in range(0,k):
                queue.append(queue[0])
                queue.popleft()
            queue.pop()   
        return queue[0]
        