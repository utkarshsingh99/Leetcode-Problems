class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        xd, yd = abs(sx-fx), abs(sy-fy)

        if max(xd, yd) > t or (sx == fx and sy == fy and t == 1):
            return False
        else:
            return True
        