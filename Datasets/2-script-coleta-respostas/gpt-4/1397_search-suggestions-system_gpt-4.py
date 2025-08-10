class Solution:
    def suggestedProducts(self, P: List[str], S: str) -> List[List[str]]:
        P.sort()
        result = []
        prefix = ""
        for char in S:
            prefix += char
            suggestions = [product for product in P if product.startswith(prefix)]
            result.append(suggestions[:3])
        return result