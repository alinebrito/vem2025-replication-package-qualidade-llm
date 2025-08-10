class Solution:
    def __init__(self, length: int):
        self.snapshots = [[] for _ in range(length)]
        self.cur_id = 0

    def set(self, index: int, val: int) -> None:
        if self.cur_id == len(self.snapshots[index]):
            self.snapshots[index].append(val)
        else:
            self.snapshots[index][self.cur_id] = val

    def snap(self) -> int:
        self.cur_id += 1
        return self.cur_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id < len(self.snapshots[index]):
            return self.snapshots[index][snap_id]
        return 0