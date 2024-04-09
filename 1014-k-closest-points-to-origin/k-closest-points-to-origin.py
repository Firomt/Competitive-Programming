class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
     
        heap = []  # min-heap
        for i, (x, y) in enumerate(points):
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, i))

        ans = []
        for _ in range(k):
            dist, index = heapq.heappop(heap)
            ans.append(points[index])

        return ans

        
            
            