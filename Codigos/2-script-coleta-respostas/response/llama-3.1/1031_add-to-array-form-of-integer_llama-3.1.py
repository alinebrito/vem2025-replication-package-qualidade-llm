class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_as_int = int(''.join(map(str, num))) + k
        return [int(digit) for digit in str(num_as_int)]