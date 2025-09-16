class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        current = nums[0]
        for num in nums[1:]:
            if gcd(current, num) > 1:
                current = lcm(current, num)
                while stack and gcd(current, stack[-1]) > 1:
                    current = lcm(current, stack.pop())
            else:
                stack.append(current)
                current = num
        stack.append(current)
        return stack
