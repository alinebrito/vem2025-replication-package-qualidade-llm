class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(ip):
            ip = ip.split('.')
            for i in ip:
                if (len(i) > 1 and i[0] == '0') or not (0 <= int(i) <= 255):
                    return False
            return len(ip) == 4

        def isIPv6(ip):
            ip = ip.split(':')
            hexdigits = '0123456789abcdefABCDEF'
            if len(ip) != 8:
                return False
            for i in ip:
                if len(i) < 1 or len(i) > 4 or all(c not in hexdigits for c in i):
                    return False
            return True

        if isIPv4(IP):
            return "IPv4"
        elif isIPv6(IP):
            return "IPv6"
        else:
            return "Neither"