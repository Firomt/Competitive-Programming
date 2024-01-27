class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        fullA=capacityA
        fullB=capacityB
        i=0
        j=len(plants)-1
        count=0
        while i<j and( i<len(plants) and j<len(plants)):
            if plants[i]<=capacityA:
                capacityA-=plants[i]
                #i+=1
            else:
                capacityA+=fullA-capacityA
                capacityA-=plants[i]
                count+=1
                
                #i+=1
            if plants[j]<=capacityB:
                capacityB-=plants[j]
                #j-=1
            else:
                capacityB+=fullB-capacityB
                capacityB-=plants[j]
                count+=1
                #j-=1
            i+=1
            j-=1
        if i==j:
            if capacityA>capacityB and plants[i]<=capacityA:
                capacityA-=plants[i]
            elif capacityA>capacityB and plants[i]>capacityA :
                capacityA+=fullA-capacityA
                capacityA-=plants[i]
                count+=1
            elif capacityA<capacityB and plants[i]<=capacityB:
                capacityB-=plants[i]
            elif capacityA<capacityB and plants[i]>capacityB:
                capacityB+=fullB-capacityB
                capacityB-=plants[i]
                count+=1
            elif capacityA==capacityB and plants[i]<=capacityA:
                capacityA-=plants[i]
            else:
                capacityA+=fullA-capacityA
                capacityA-=plants[i]
                count+=1


                
        
        return count
    

        