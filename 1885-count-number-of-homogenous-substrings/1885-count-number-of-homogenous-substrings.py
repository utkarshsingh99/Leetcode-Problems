class Solution:
    def countHomogenous(self, s: str) -> int:

        ind, last, cur_count = 0, None, 0
        ans = 0
        while ind != len(s):
            # print(last, s[ind])
            if last is not None and s[ind] != last:
                ans += (cur_count*(cur_count+1))//2
                cur_count = 1
            else:
                cur_count += 1
            last = s[ind]
            ind += 1

        ans += (cur_count*(cur_count+1))//2
        return ans % 1000000007