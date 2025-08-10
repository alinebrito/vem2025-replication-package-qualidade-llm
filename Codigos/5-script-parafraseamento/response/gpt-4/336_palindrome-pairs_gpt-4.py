class Solution:
    def palindromeWords(self, words):
        return [word for word in words if self.is_palindrome(word)]
    
    def is_palindrome(self, check):
        return check == check[::-1]