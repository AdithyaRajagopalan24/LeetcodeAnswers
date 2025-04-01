class Solution:
    def simplifyPath(self, path: str) -> str:
        directoryStack = []
        path = path.split("/")
        for element in path:
            if directoryStack and element == "..":
                directoryStack.pop()
            elif element not in [".", "", ".."]:
                directoryStack.append(element)
        return "/" + "/".join(directoryStack)