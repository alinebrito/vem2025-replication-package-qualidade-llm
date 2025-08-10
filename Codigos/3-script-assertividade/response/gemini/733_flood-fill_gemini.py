class Solution:
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image
        self.fill(image, sr, sc, color, image[sr][sc])
        return image
        
    def fill(self, image, sr, sc, color, cur):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != cur:
            return
        image[sr][sc] = color
        self.fill(image, sr + 1, sc, color, cur)
        self.fill(image, sr - 1, sc, color, cur)
        self.fill(image, sr, sc + 1, color, cur)
        self.fill(image, sr, sc - 1, color, cur) 