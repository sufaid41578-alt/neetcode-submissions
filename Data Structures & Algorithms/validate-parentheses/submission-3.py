class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={')':'(',']':'[','}':'{'}
        for i in s:
            if i in pairs.values():
                stack.append(i)
            elif not stack:
                return False
            elif stack[-1]==pairs[i]:
                stack.pop()
            else:
                return False
        return not stack



