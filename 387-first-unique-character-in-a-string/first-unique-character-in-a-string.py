class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique=Counter(s)
        for i in unique:
            if unique[i]==1:
                return s.index(i)

        return -1
        
        