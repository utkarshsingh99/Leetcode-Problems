class Solution:
    def finalString(self, s: str) -> str:
        ans = ""
        for i in s:
            if i != 'i':
                ans += i
            else:
                a = list(ans)
                a.reverse()
                ans = ''.join(a)
        
        return ans