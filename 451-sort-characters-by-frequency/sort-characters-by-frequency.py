class Solution:
    def frequencySort(self, s: str) -> str:
        cnt=Counter(s)
        sorted_chars=""
        for char, freq in cnt.most_common():
            sorted_chars += char*freq
        return sorted_chars