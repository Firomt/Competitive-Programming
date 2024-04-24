class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cards_hash={}
        if len(cards)==1:
            return -1
        i=0
        j=i+1
        min_consec=float('inf')
        for i,c in enumerate(cards):
            if c in cards_hash:
                min_consec=min(min_consec, i-cards_hash[c]+1)
                del cards_hash[c]
            cards_hash[c]=i
       
        if min_consec==float('inf'):
            return -1
        return min_consec


        