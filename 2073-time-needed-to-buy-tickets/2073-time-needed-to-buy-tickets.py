class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t=0
        tick_k=tickets[k]
        for i in range(len(tickets)):
            if k<i and tickets[i]>= tick_k:
                t+=tick_k-1
            elif tickets[i] < tick_k:
                t+=tickets[i]
            else:
                t+=tick_k
        return t


                
            