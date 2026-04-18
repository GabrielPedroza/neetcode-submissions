class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '/': lambda x, y: int(x / y),
            '*': lambda x, y: x * y,
        }

        def recurse(token):
            if token not in operations:
                return int(token)
            
            y, x = recurse(tokens.pop()), recurse(tokens.pop())

            return operations[token](x, y)
        
        return recurse(tokens.pop())