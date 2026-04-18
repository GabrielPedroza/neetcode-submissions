class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0: return False

        stack = []

        brackets = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

        for ch in s:
            if not stack or ch not in brackets:
                stack.append(ch)
            else:
                if stack.pop() != brackets[ch]:
                    return False
        
        if stack: return False
        
        return True
