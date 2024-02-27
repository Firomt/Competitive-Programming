class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        index_map=defaultdict(list)
        res=[0]*len(arr)
        for i,n in enumerate(arr):
            index_map[n].append(i)
        
        for indices in index_map.values():
            total=sum(indices)
            size=len(indices)
            leftsum=0
            for i,ind in enumerate(indices):
                res[ind]=i*ind-leftsum + (total-leftsum-ind)-(size-i-1)*ind
                leftsum+=ind
        return res

        


        
        