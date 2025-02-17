"""
Tc: O(k^N/k)
SP: O(n)
"""
class Solution:
    def expand(self, s: str) -> List[str]:
        parsed = []
        i = 0
        while i < len(s):
            if s[i] == "{":
                i += 1
                curr = []
                while i < len(s) and s[i] != "}":
                    if s[i].isalpha():
                        curr.append(s[i])
                    i += 1
                parsed.append(sorted(curr))
            else:
                parsed.append([s[i]])
            i += 1
        res = []

        def backtrack(i, path):
            if i >= len(parsed):
                res.append("".join(path))
                return
            for j in range(len(parsed[i])):
                path.append(parsed[i][j])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
