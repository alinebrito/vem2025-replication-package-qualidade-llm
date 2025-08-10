class Solution:
  def reverseString(self, s):
    """
    Reverses a string in-place.

    Args:
      s: A list of characters representing the string to reverse.

    Returns:
      None. The input string is modified in-place.
    """
    left, right = 0, len(s) - 1
    while left < right:
      s[left], s[right] = s[right], s[left]
      left += 1