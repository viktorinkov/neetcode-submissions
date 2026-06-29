class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += (s)
            ans += (";")

        return ans

    def decode(self, s: str) -> List[str]:
        arr = s.split(";")
        arr.pop()
        return arr

