class Solution:
class SnapshotArray:
    def __init__(self, length: int):
        self.cur_id = 0
        self.arr = [0] * length
        self.snapshots = [[self.arr[:]] for _ in range(1)]

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        self.snapshots.append(self.arr[:])
        self.cur_id += 1
        return self.cur_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id][index]