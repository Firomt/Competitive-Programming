class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_freq=[]
        freq_hash=defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in freq_hash:
                freq_hash[nums[i]]+=1
            else:
                freq_hash[nums[i]]=1

        while k>0:
            cand_key=max(freq_hash, key=freq_hash.get)
            top_freq.append(cand_key)
            k-=1
            del freq_hash[cand_key]
        return top_freq
        