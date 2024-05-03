class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_score=0
        l, r = 0, len(cardPoints)-k
        total_pts= sum(cardPoints[r:])
        max_score=total_pts

        while r < len(cardPoints):
            total_pts += cardPoints[l]-cardPoints[r]
            max_score=max(max_score, total_pts)
            r+=1
            l+=1
        return max_score

        
     
        