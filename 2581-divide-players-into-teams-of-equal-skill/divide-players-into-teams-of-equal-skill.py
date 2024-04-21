class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        chem = skill[0] * skill[n-1]
        tot_skill = skill[0] + skill[n-1]
        if n==2:
            return skill[0]*skill[1]
        
        i, j=1, n-2
        while i<j:
            if skill[i]+ skill[j]==tot_skill:
                chem += skill[i] * skill[j]
            else:
                return -1
            i+=1
            j-=1
        return chem

        

        