class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textCount=Counter(text)
        balloon=Counter("balloon")
        res=float("inf")

        for c in balloon:
            res=min(res, textCount[c] //balloon[c])
        return res
        