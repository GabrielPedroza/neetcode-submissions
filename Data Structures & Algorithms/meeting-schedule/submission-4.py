"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not len(intervals): return True
        intervals.sort(key = lambda x : x.start)
        output = [intervals[0]]

        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            localEnd = output[-1].end

            if start < localEnd:
                return False
            
            output.append(interval)

        return True

