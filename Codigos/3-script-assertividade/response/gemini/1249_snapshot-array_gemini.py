class Solution:
class SnapshotArray:
    def __init__(self, length: int):
        self.cur_id = 0
        self.snap_shot = [[[-1, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.snap_shot[index].append([self.cur_id, val])

    def snap(self) -> int:
        self.cur_id += 1
        return self.cur_id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = self.binary_search(self.snap_shot[index], snap_id)
        return self.snap_shot[index][i][1]

    def binary_search(self, arr, target):