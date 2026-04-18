class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        stack = []

        for pos, speed in posSpeed:
            timeToFinish = (target - pos) / speed
            if not stack or stack[-1] < timeToFinish:
                stack.append(timeToFinish)
        
        return len(stack)