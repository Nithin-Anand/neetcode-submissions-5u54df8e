class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                last_paren = stack.pop()
                if s[i] == ')':
                    if last_paren != '(':
                        return False
                elif s[i] == '}':
                    if last_paren != '{':
                        return False
                elif s[i] == ']':
                    if last_paren != '[':
                        return False
        if len(stack) > 0:
            return False
        else:
            return True
