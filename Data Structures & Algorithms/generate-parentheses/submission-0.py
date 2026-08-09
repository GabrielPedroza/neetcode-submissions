class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def backtrack(openP, closedP, total):
            if len(total) == n * 2:
                output.append(total)
                return

            if openP < n:
                backtrack(openP + 1, closedP, total + '(')
            
            if openP > closedP:
                backtrack(openP, closedP + 1, total + ')')

        
        backtrack(0, 0, '')

        return output