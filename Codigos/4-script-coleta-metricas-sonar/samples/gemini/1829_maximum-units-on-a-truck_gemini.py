class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda a:-a[1])
        maxUnits = 0
        for box in boxTypes:
            if truckSize >= box[0]:
                maxUnits += box[0] * box[1]
                truckSize -= box[0]
            else:
                maxUnits += truckSize * box[1]
                break
        return maxUnits