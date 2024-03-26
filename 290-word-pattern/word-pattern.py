class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map={}
        s=list(s.split())
        if len(s)>len(pattern) or len(s)<len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in hash_map:
                if s[i] != hash_map[pattern[i]]:
                    return False
            else:
                if s[i] in hash_map.values():
                    return False
                hash_map[pattern[i]]=s[i]
        return True



        