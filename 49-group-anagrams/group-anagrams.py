class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
  
        hash_table = {}
        anagrams = []
        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            if sorted_str in hash_table:
                anagrams[hash_table[sorted_str]].append(strs[i])
            else:
                hash_table[sorted_str] = len(anagrams)
                anagrams.append([strs[i]])
        return anagrams

        