class Solution:
    def fullJustify(self, words, maxWidth):
        lines = self.constructLines(words, maxWidth)
        lines = self.addSpaces(lines, maxWidth)
        lines = list(map(lambda x : "".join(x), lines))
        return lines
    
    def constructLines(self, words, maxWidth):
        lines = []
        
        # Construct words per line
        wordLensInPara = list(map(len, words))
        i, j = 0, 0
        while i < len(words):
            while j < len(words):
                width = sum(wordLensInPara[i:j+1]) + (j-i)
                if width > maxWidth: break
                else: j += 1
            lines.append(words[i:j])
            i = j = j
        
        return lines
    
    def addSpaces(self, lines, maxWidth):
        for line in lines:
            words = len(line)
            wordLensInLine = list(map(len, line))
            lineLen = sum(wordLensInLine)
            numOfSpaces = maxWidth - lineLen
            
            # Standard line
            if lines.index(line) < len(lines)-1:
                if words == 1: # One word
                    line[0] += " " * numOfSpaces
                else: # Multiple words
                    numOfSpacesPerWord, extraSpaces = divmod(numOfSpaces,words-1)
                    for i in range(len(line)-1):
                        line[i] += " " * numOfSpacesPerWord

                        if extraSpaces > 0:
                            line[i] += " "
                            extraSpaces -= 1
            # Last line
            else:
                for i in range(len(line)-1):
                    line[i] += " "
                    numOfSpaces -= 1
                line[-1] += " " * numOfSpaces
            
        return lines