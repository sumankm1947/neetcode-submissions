class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        n = len(tokens)
        if n == 1:
            return int(tokens[0])
        
        for token in tokens:
            match token:
                case '+':
                    int2 = stack.pop()
                    int1 = stack.pop()
                    stack.append(int1 + int2)
                case '-':
                    int2 = stack.pop()
                    int1 = stack.pop()
                    stack.append(int1 - int2)
                case '*':
                    int2 = stack.pop()
                    int1 = stack.pop()
                    stack.append(int1 * int2)
                case '/':
                    int2 = stack.pop()
                    int1 = stack.pop()
                    stack.append(int(int1 / int2))
                case _:
                    stack.append(int(token))
            print(stack[-1])
            
        return stack.pop()
