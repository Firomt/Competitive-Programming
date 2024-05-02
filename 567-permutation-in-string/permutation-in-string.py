from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d=Counter(s1)
        ws=0
        matched=0
        for we in range(len(s2)):
            c=s2[we]
            if c in d:
                d[c]-=1
                if d[c]==0:
                    matched+=1
            if we-ws+1==len(s1):
                if len(d)==matched:
                    return True
                else:
                    a=s2[ws]
                    if a in d:
                        if d[a]==0:
                            matched-=1
                        d[a]+=1
                ws+=1
        return False
            
        