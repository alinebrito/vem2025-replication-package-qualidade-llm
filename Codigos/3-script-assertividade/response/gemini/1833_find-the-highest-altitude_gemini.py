class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        current_altitude = 0
        for i in range(len(gain)):
            current_altitude += gain[i]
            max_altitude = max(max_altitude, current_altitude)
        return max_altitude