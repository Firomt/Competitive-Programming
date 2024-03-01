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

        # Hash = {}
        # anagrams=[ ]
        # for i in range(len(strs)):
        #     if ''.join(sorted(strs[i])) in Hash:
        #         anagrams[Hash[''.join(sorted(str[i]))]].append(strs[i])
        #     else:
        #         Hash[''.join(sorted(strs[i]))]=i
        #         anagrams.append(list(strs[i]))

        return anagrams
        