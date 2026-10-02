class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #counter function
        return Counter(s) == Counter(t)