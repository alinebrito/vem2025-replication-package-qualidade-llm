class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    """
    Given a string of digits, return all possible letter combinations.
    """
    # Create a dictionary mapping digits to their corresponding letters
    digit_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    combinations = []
    if not digits:
        return combinations

    def backtrack(current_combination, index):
      # If we've reached the end of the digits, add the combination
      if index == len(digits):
        combinations.append(current_combination)
        return

      # Get the letters for the current digit
      letters = digit_letters[digits[index]]
      
      # Loop through each letter and add it to the combination
      for letter in letters:
        backtrack(current_combination + letter, index + 1)

    backtrack("", 0)
    return combinations