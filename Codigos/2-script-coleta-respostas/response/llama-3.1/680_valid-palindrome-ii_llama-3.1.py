class Solution:
    def validPalindrome(self, s: str) -> bool:
        def verify(s, left, right, deleted):
            while left < right:
                if s[left]!= s[right]:
                    if not deleted:
                        return verify(s, left + 1, right, True) or verify(s, left, right - 1, True)
                    return False
                left += 1
                right -= 1
            return True

        return verify(s, 0, len(s) - 1, False)