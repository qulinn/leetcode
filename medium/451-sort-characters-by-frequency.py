class Solution:
    def frequencySort(self, s: str) -> str:
        c = collections.Counter(s)
        string_builder = []
        for letter,freq in c.most_common():
            string_builder.append(letter*freq)
        return "".join(string_builder)

