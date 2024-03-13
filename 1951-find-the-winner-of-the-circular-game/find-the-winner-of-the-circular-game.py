class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()
        for i in range(1,n+1):
            queue.append(i)   
        while len(queue) > 1:
            for i in range(0,k):  #shift the array k times
                queue.append(queue[0])
                queue.popleft()
            queue.pop() # the element we get at exactly k'th shift is the one to be removed and this elemnt will be at the end of the queue after shifting it so we pop this element  
        return queue[0]  #after popping all elements one element will be left and that is the winner
        