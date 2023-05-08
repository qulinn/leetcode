class Solution:
    def reverseVowels(self, s: str) -> str:
        #if s doesn't include any vowels?
        #does s include uppercase?

        left = 0
        right = len(s)-1
        list_s = list(s)
        vowel = set("aeiouAEIOU")
        
        while left < right:
            if list_s[left] in vowel and list_s[right] in vowel:
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left += 1
                right -= 1
            if list_s[left] not in vowel:
                left += 1
            if list_s[right] not in vowel:
                right -= 1
        return "".join(list_s)