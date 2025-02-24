'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

class solution:
    def canConstruct(self, a: str, b: str):
        counter = {}
        for c in b:
            counter[c] = counter.get(c,0) + 1
        for i in range(len(a)):
            if a[i] in counter:
                if counter[a[i]] == 1:
                    del counter[a[i]]
                else:
                    counter[a[i]]-=1
            else:
                return False
        return True
