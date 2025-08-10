class Solution:
  def sortColors(self, nums):
    red, white = 0, 0  # red pointer and white pointer

    for i in range(len(nums)):
      if nums[i] == 0:
        nums[i], nums[red] = nums[red], nums[i]
        red += 1
        white += 1 if white < red else 0  # move white only if behind red
      elif nums[i] == 1:
        nums[i], nums[white] = nums[white], nums[i]
        white += 1