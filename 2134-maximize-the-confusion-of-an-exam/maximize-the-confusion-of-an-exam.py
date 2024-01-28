class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left=0
        Tcount=0
        Fcount=0
        maxConsec=0
        for right in range(len(answerKey)):
            if answerKey[right]=="T":
                Tcount+=1
            else:
                Fcount+=1

            while min(Tcount,Fcount) > k:
                if answerKey[left]=="T":
                    Tcount-=1
                else:
                    Fcount-=1
                left+=1
            maxConsec= max(maxConsec, right-left+1)
        return maxConsec

