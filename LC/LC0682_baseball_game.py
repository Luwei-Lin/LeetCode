class Solution:
    def calPoints(self, ops):
        sum = 0
        stack = []
        for e in ops:
            if e == "C" and len(stack) > 0:
                stack.pop()
            elif e == "D":
                new_e = 2 * int(stack[-1])
                stack.append(new_e)
            elif e == "+" and len(stack) >= 2:
                new_e = int(stack[-1]) + int(stack[-2])
                stack.append(new_e)
            else:
                stack.append(int(e))
        for e in stack:
            sum += e
        return sum96
def main():
    ops_0 = ["5","2","C","D","+"]
    ops_1 = ["1"]
    ops_2 = ["5","-2","4","C","D","9","+","+"]
    print(Solution().calPoints(ops_0))
main()