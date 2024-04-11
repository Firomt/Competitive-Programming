class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count, avg_sum, i =0 , 0, 0
        avg_sum=sum(arr[:k])
        if (avg_sum/k) >= threshold:
                count+=1
        for j in range(k, len(arr)):
            avg_sum=avg_sum-arr[i]+arr[j]
            if (avg_sum/k) >= threshold:
                count+=1
            i+=1
        return count

        