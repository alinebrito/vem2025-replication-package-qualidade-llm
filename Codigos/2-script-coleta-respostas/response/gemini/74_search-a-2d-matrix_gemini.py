class Solution:
    def searchMatrix(self, matrix, target):
        """
        Searches for a target value in a sorted matrix.

        Args:
            matrix: A 2D list of integers representing the sorted matrix.
            target: The integer to search for.

        Returns:
            True if the target is found in the matrix, False otherwise.
        """

        if not matrix or target is None:
            return False

        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1

        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1

        return False