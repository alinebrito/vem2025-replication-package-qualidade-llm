class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda a:-a[1])
        total_units = 0
        for boxes, units_per_box in boxTypes:
            if truckSize >= boxes:
                total_units += boxes * units_per_box
                truckSize -= boxes
            else:
                total_units += truckSize * units_per_box
                break
        return total_units