class Solution:
  def trap(self, height: list[int]) -> int:
    total_water = 0
    left_max, right_max = 0, 0
    left, right = 0, len(height) - 1

    while left < right:
      left_max = max(left_max, height[left])
      right_max = max(right_max, height[right])

      # Water trapped is limited by the shorter wall
      water_level = min(left_max, right_max)

      # Subtract the height of the current bar from the water level
      if height[left] < water_level:
        total_water += water_level - height[left]
        left += 1
      elif height[right] < water_level:
        total_water += water_level - height[right]
        right -= 1
      else:
        # Move the pointer towards the shorter wall
        if left_max < right_max:
          left += 1
        else:
          right -= 1

    return total_water