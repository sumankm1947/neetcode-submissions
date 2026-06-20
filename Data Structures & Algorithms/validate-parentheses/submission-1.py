class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if stack:
                    last_c = stack[-1]
                    if (c == ')' and last_c == '(') or (c == '}' and last_c == '{') or (c == ']' and last_c == '['):
                        stack = stack[0: -1]
                    else:
                        return False
                else:
                    return False
        
        if stack: return False
        return True