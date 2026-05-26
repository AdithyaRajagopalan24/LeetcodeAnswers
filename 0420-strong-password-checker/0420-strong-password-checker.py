class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        passwordLen = len(password)
        missingTypes = 3 - sum(bool(re.search(pattern, password)) for pattern in ['[a-z]', '[A-Z]', '[0-9]'])
        if passwordLen < 6:
            return max(6 - passwordLen, missingTypes)
        repeatGroups = []
        for ignoredChar, group in groupby(password):
            groupLen = len(list(group))
            if groupLen >= 3:
                heappush(repeatGroups, (groupLen % 3, groupLen))
        operations = 0

        while repeatGroups and passwordLen > 20:
            modClass, groupLen = heappop(repeatGroups)
            if groupLen > 3:
                heappush(repeatGroups, ((groupLen - 1) % 3, groupLen - 1))
            passwordLen -= 1
            operations += 1

        replacements = 0
        for modClass, groupLen in repeatGroups:
            replacements += groupLen // 3

        return operations + max(0, passwordLen - 20) + max(replacements, missingTypes)