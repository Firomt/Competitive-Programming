class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        # formula -> suffix - (distance from right * index value) + prefix - (distance from left * index value)
        d = defaultdict(list)
        prefix = defaultdict(list)
        suffix = defaultdict(list)
        for i in range(len(arr)):
            if arr[i] in d:
                prefix[arr[i]].append(prefix[arr[i]][-1] + i)
            else:
                prefix[arr[i]].append(i)
            d[arr[i]].append(i)

        for i, val in d.items():
            summ = 0
            for idx in range(len(val)-1, -1, -1):
                summ += val[idx]
                suffix[i].append(summ)
            suffix[i] = suffix[i][::-1]

        ans = [0] * len(arr)
        for i, val in suffix.items():
            n = len(val)
            for j in range(n):
                summ = (abs(prefix[i][j] - ((j + 1) * d[i][j])) + abs(suffix[i][j] - ((n - j)* d[i][j])))
                ans[d[i][j]] = summ
        return ans



        


        
        