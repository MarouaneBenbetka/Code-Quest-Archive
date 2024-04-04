# https://leetcode.com/problems/count-pairs-of-similar-strings/

class Solution:
    def similarPairs(self, words):
        words_clean = [sorted(set(word)) for word in words]

        cpt = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words_clean[i] == words_clean[j]:
                    cpt += 1

        return cpt
