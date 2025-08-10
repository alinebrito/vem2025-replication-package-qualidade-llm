class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        left, right, max_fruits = 0, 0, 0
        fruit_count = {}
        
        while right < len(tree):
            if tree[right] in fruit_count:
                fruit_count[tree[right]] += 1
            else:
                fruit_count[tree[right]] = 1
            
            while len(fruit_count) > 2:
                fruit_count[tree[left]] -= 1
                if fruit_count[tree[left]] == 0:
                    del fruit_count[tree[left]]
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
            right += 1
        
        return max_fruits