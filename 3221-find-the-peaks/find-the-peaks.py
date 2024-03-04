class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks=[]
        for i in range(len(mountain)):
            if i==0 or i==len(mountain)-1:
                continue
            if mountain[i] > mountain[i-1] and mountain[i]> mountain[i+1]:
                peaks.append(i)
        return peaks
        