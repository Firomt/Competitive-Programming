class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i, j = 0, 1
        if len(arr)<3:
            return False
        if arr[i]< arr[j]:
            while (arr[i] < arr[j]) and (i < len(arr) and j< len(arr)-1):
                i+=1
                j+=1
            if j==len(arr)-1 and (arr[j]>arr[i] or arr[j]==arr[i]):
                return False
            elif arr[j]>arr[i] or arr[j]==arr[i]:
                return False
            elif arr[i] > arr[j] :
                while (arr[i]>arr[j]) and (i < len(arr) and j< len(arr)-1):
                    i+=1
                    j+=1
                if arr[i]<arr[j] or arr[i]==arr[j]:
                    return False
            return True
        return False
            

            
        