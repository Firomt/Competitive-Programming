class Solution(object):
    def topKFrequent(self, nums, k):
        top_freq=[]
        freq_hash=Counter(nums)
        
        while k>0:
            cand_key=max(freq_hash, key=freq_hash.get)
            top_freq.append(cand_key)
            k-=1
            del freq_hash[cand_key]
        return top_freq
        
        