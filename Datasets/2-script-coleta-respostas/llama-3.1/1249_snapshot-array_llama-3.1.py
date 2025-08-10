class Solution:
    def __init__(self, length: int):
        self.arr = [[0] for _ in range(length)]
        self.cur_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append(val)

    def snap(self) -> int:
        self.cur_id += 1
        return self.cur_id -1

    def get(self, index: int, snap_id: int) -> int:
        return self.arr[index][snap_id+1]