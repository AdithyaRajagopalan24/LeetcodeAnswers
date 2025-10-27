from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        totalBeams = 0
        prevDevices = 0

        for row in bank:
            deviceCount = row.count('1')
            if deviceCount > 0:
                totalBeams += prevDevices * deviceCount
                prevDevices = deviceCount

        return totalBeams
