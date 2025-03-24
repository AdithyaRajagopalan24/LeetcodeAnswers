class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetinglessDays = 0
        lastHeldMeetingEnd = 0
        meetings.sort()

        for start, end in meetings:
            if start > lastHeldMeetingEnd + 1:
                meetinglessDays += start - lastHeldMeetingEnd - 1
            lastHeldMeetingEnd = max(lastHeldMeetingEnd, end)
        meetinglessDays += days - lastHeldMeetingEnd
        return meetinglessDays
