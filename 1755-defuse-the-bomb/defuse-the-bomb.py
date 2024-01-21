class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        sum_list = []

        if (k > 0):
            new_code = code + code[:k]
            for i in range(1, len(code) + 1):
                sum_list.append(sum(new_code[i : i + k]))
            return sum_list

        elif (k < 0):
            new_code = code[k:] + code
            for i in range(len(code)):
                sum_list.append(sum(new_code[i : i + abs(k)]))
            return sum_list
            
        elif (k == 0):
            return [0 for i in range(len(code))]

        return [0, 0]
        