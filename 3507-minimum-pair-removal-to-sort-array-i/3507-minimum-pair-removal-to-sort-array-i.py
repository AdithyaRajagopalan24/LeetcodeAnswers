class Solution:
    def minimumPairRemoval(self, numbers: list[int]) -> int:
        operations = 0

        while True:
            sortedFlag = True
            for index in range(len(numbers) - 1):
                if numbers[index] > numbers[index + 1]:
                    sortedFlag = False
                    break

            if sortedFlag:
                return operations

            minPairSum = None
            minPairIndex = 0

            for index in range(len(numbers) - 1):
                pairSum = numbers[index] + numbers[index + 1]
                if minPairSum is None or pairSum < minPairSum:
                    minPairSum = pairSum
                    minPairIndex = index

            numbers[minPairIndex] = minPairSum
            del numbers[minPairIndex + 1]
            operations += 1
