class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        fullCapacity=capacity
        i,steps=0,0
        while i < len(plants):
            if capacity-plants[i]>=0:
                capacity-=plants[i]
                steps+=1
                i+=1
            else:
                steps+=i
                capacity+=fullCapacity-capacity
                steps+=i
        return steps       