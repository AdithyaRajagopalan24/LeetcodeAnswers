class Solution:
    def numRabbits(self, answers):
        answers.sort()
        rabbitCount = 0
        count = 0
        for i in range(len(answers)):
            if answers[i] == 0:
                rabbitCount += 1  
            elif (i == 0 or count == 0) or answers[i] != answers[i - 1]:
                rabbitCount += answers[i] + 1  
                count = answers[i]
            else:
                count -= 1 
        return rabbitCount