class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j, pos = 0, 0, 0
        while j < len(arr2) and pos < len(arr1):
            i = pos
            while i < len(arr1):
                if arr1[i] == arr2[j]:
                    arr1[pos], arr1[i] = arr1[i], arr1[pos]
                    pos += 1
                i += 1
            j += 1
        
        k=len(arr2)-1
        while ( k in range(len(arr1))) and (arr1[k] in arr2):
            k+=1
        if k < len(arr1):
            for y in range(k, len(arr1)-1):
                min_idx = y
                for z in range(y+1, len(arr1)):
                    if arr1[min_idx] > arr1[z]:
                        min_idx = z
                arr1[y], arr1[min_idx] = arr1[min_idx], arr1[y]

        return arr1