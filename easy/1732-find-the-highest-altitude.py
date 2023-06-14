class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        highest_point = current_altitude

        for i in gain:
            current_altitude += i
            highest_point = max(highest_point, current_altitude)
        
        return highest_point
