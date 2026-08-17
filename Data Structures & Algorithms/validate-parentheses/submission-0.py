class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for brackets in s:
            if brackets in close_to_open:
                if not stack or stack[-1] != close_to_open[brackets]:
                    return False
                stack.pop()
            else:
                stack.append(brackets)

            
        return len(stack) == 0