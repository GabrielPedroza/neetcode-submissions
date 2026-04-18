class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '/': lambda x, y: int(x / y),
            '*': lambda x, y: x * y,
        }

        stack = []

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                y, x = stack.pop(), stack.pop()
                stack.append(operations[token](x, y))
        
        return stack.pop()
