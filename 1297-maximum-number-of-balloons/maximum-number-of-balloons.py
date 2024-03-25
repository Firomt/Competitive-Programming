class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textCount=Counter(text)
        balloon=Counter("balloon")
        ans=float("inf")

        for c in balloon:
            ans=min(ans, textCount[c] //balloon[c])
        return ans
        