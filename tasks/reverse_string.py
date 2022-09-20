from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        

if __name__ == "__main__":
    result = Solution()
    s = ["h","e","l","l","o"]
    result.reverseString(s)
    print(s)
        