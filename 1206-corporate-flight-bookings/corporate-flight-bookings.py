class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        path = [0] * (n + 2)
        ans = [0] * n
        cnt = 0
        for x in bookings:
            path[x[0]] += x[2]
            path[x[1] + 1] -= x[2]
        for i in range(1, n + 1):
            cnt += path[i]
            ans[i - 1] = cnt
        return ans


        