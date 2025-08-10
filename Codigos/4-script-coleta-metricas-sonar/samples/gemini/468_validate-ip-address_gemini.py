class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            parts = IP.split('.')
            if len(parts) != 4:
                return "Neither"
            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255 or (part[0] == '0' and len(part) > 1):
                    return "Neither"
            return "IPv4"
        elif ':' in IP:
            parts = IP.split(':')
            if len(parts) != 8:
                return "Neither"
            for part in parts:
                if len(part) == 0 or len(part) > 4:
                    return "Neither"
                for c in part:
                    if not (c.isdigit() or ('a' <= c <= 'f') or ('A' <= c <= 'F')):
                        return "Neither"
            return "IPv6"
        else:
            return "Neither"