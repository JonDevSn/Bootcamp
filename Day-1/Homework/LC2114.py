class Solution(object):
    def mostWordsFound(self, sentences):
        max_count = 0

        for i in range(len(sentences)):
            count = len(sentences[i].split())
            max_count = max(max_count, count)

        return max_count