class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hash_table={}
        ans=[]
        for i in range(len(heights)):
            hash_table[heights[i]]=names[i]

        for i in range(0,len(heights)-1):  
            for j in range(len(heights)-1):  

                if(heights[j]<heights[j+1]): 
                    heights[j],heights[j+1]=heights[j+1],heights[j] 
                    
        for i in range(len(heights)):
            ans.append(hash_table[heights[i]])
        return ans


        