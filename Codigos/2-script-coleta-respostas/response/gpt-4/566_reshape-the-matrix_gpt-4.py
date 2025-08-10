class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten = []
        for row in mat:
            flatten.extend(row)
        if len(flatten) != r * c:
            return mat  
        return [flatten[i * c:(i + 1) * c] for i in range(r)]