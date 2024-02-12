class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_arr = arr[:mid]
                right_arr = arr[mid:]

             
                merge_sort(left_arr)
                merge_sort(right_arr)

               
                merge(left_arr, right_arr, arr)

       
        def merge(left_arr, right_arr, arr):
            i = j = k = 0

           
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1

        
        merge_sort(arr)
        return arr