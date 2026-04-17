class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}
        if len(s) != len(t): return False
        for letter in list(s):
            table[letter] = table.get(letter, 0) + 1
        for letter in list(t):
            table[letter] = table.get(letter, 0) - 1
        return not any(count != 0 for count in table.values())

        