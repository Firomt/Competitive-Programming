class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        turns=abs(target[0])+abs(target[1])
        for i in ghosts:
            catch=abs(i[0]-target[0])+abs(i[1]-target[1])
            if catch <= turns:
                return False
        return True
        