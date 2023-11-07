class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        times = [dist[i]/speed[i] for i in range(n)]

        count = 0
        times.sort()
        for i in range(n):
            if times[i] > i:
                count += 1
            else:
                break
        return count
        