class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        turns=abs(target[0])+abs(target[1])  #the number of turns you take to reach the target
        for i in ghosts:
            catch=abs(i[0]-target[0])+abs(i[1]-target[1])   #the number of turns the ghost at a point need to take to catch up to the target
            if catch <= turns:  #if the number of turns needed for the ghost to catch up to the target
                return False  #if it is lessthan the actual turns needed to reach the target , then the ghost can catch up to the target so return false
        return True          #all the catch up turns are greater than the actual number of turn needed to reach the target so no ghost can catch up
        