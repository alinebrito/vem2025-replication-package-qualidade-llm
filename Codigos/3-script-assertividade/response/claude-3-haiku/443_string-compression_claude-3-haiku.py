class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        for read in range(len(chars)):
            if read == 0 or chars[read] != chars[read-1]:
                chars[write] = chars[read]
                write += 1
            count = 1
            while read+1 < len(chars) and chars[read+1] == chars[read]:
                count += 1
                read += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            read += 1
        return write