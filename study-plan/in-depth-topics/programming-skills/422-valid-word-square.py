# editorial approach 2

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for word_num in range(len(words)):
            for char_pos in range(len(words[word_num])):
                # char_pos (current 'row' word) is bigger than column word
                # or word_num (current 'column' word) is bigger than row word
                # or characters at index (word_num, char_pos) and (char_pos, word_num) aren't equal
                if char_pos >= len(words) or word_num >= len(words[char_pos]) or \
                    words[word_num][char_pos] != words[char_pos][word_num]:
                    return False
        return True
