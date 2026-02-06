class Solution:
    def mostBooked(self, roomCount: int, meetings: List[List[int]]) -> int:
        meetingCount = [0] * roomCount
        roomAvailableAt = [0] * roomCount
        meetings.sort()

        for startTime, endTime in meetings:
            assigned = False
            earliestRoom = 0
            earliestTime = float("inf")

            for roomIndex in range(roomCount):
                if roomAvailableAt[roomIndex] < earliestTime:
                    earliestTime = roomAvailableAt[roomIndex]
                    earliestRoom = roomIndex

                if roomAvailableAt[roomIndex] <= startTime:
                    meetingCount[roomIndex] += 1
                    roomAvailableAt[roomIndex] = endTime
                    assigned = True
                    break

            if not assigned:
                meetingCount[earliestRoom] += 1
                roomAvailableAt[earliestRoom] += endTime - startTime

        maxMeetings = -1
        resultRoom = -1

        for roomIndex in range(roomCount):
            if meetingCount[roomIndex] > maxMeetings:
                maxMeetings = meetingCount[roomIndex]
                resultRoom = roomIndex

        return resultRoom
