class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_ipv4(ip):
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or (part.startswith('0') and len(part) > 1) or not (0 <= int(part) <= 255):
                    return False
            return True

        def is_ipv6(ip):
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            for part in parts:
                if len(part) == 0 or len(part) > 4 or not all(c in '0123456789abcdefABCDEF' for c in part):
                    return False
            return True

        if '.' in queryIP and ':' in queryIP:
            return "Neither"
        if is_ipv4(queryIP):
            return "IPv4"
        if is_ipv6(queryIP):
            return "IPv6"
        return "Neither"