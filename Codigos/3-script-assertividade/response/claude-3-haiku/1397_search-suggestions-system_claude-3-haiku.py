class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ''
        for c in searchWord:
            prefix += c
            res.append([p for p in products if p.startswith(prefix)][:3])
        return res