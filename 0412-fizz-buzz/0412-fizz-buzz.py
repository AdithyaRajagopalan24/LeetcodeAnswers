class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        valList = []
        for i in range(1, n+1):
            if i%15==0:
                valList.append("FizzBuzz")
            elif i%5==0:
                valList.append("Buzz")
            elif i%3==0:
                valList.append("Fizz")
            else:
                valList.append((str)(i))
        return valList