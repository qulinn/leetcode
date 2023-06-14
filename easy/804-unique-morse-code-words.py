class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        #a: .-
        #b: -...
        #c: -.-.
        #words をMorse Codeに変換
        #Morse Codeのリストをsetにする
        #return len（set）
        
        #1 <= words[i].length <= 12
        
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse_words = []
        for w in words:
            temp = ""
            for i in w:
                temp += morse_code[ord(i)-96-1]
            morse_words.append(temp)
        
        set_words = set(morse_words)
        
        return len(set_words)
