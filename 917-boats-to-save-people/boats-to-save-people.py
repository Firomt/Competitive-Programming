class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r=0,len(people)-1
        min_boats=0
        while l <= r:
            if people[l]+people[r] <= limit:
                min_boats+=1
                l+=1
                r-=1
            else:
                r-=1
                min_boats+=1
        return min_boats

        