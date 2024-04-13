class Solution:
    def smallestNumber(self, num: int) -> int:
        to_str=str(num)
        to_str.split()
        num_lst=list(to_str)
        n=len(num_lst)
        if abs(num)< 10:
            return num
        for i in range(n):
            for j in range(i+1, n):
                if i==0:
                    if num_lst[j]=='0':
                        continue
                    elif num > 0 and num_lst[j] < num_lst[i]:
                        num_lst[i], num_lst[j]=num_lst[j], num_lst[i]
                    elif num < 0:
                        continue
                elif num > 0 and num_lst[j] < num_lst[i]:
                    num_lst[i], num_lst[j]=num_lst[j], num_lst[i]
                elif num <0 and num_lst[j] > num_lst[i]:
                    num_lst[i], num_lst[j]=num_lst[j], num_lst[i]
                    
        return int(''.join(num_lst))





      