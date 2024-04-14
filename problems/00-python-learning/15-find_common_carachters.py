# https://leetcode.com/problems/find-common-characters/


class Solution:
    def commonChars(self, words):

        words = sorted(sorted(word) for word in words)
        print(words)
        pointers = {}
        res = []

        j = 0
        while j < min(len(word) for word in words):
            c = words[0][j]

            for i, word in enumerate(words[1:]):
                print("".join(word))
                while pointers.get(i, 0) < len(word)-1 and word[pointers.get(i, 0)] < c:
                    pointers[i] = pointers.get(i, 0) + 1

                if pointers.get(i, 0) < len(word) and word[pointers.get(i, 0)] == c:
                    pointers[i] = pointers.get(i, 0) + 1
                    continue
                else:
                    break
            else:
                res.append(c)

            j += 1

        return res
