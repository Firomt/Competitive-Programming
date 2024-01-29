class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        r=0
        minOp=float('inf')
        Wcount=0
        while r<len(blocks):
            while r-l<k and r in range(len(blocks)):
                if blocks[r]=="W":
                    Wcount+=1
                r+=1
            minOp=min(Wcount,minOp)
            

            if blocks[l]=="W":
                Wcount-=1
            l+=1
        return minOp
        