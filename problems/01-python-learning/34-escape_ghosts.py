
# https://leetcode.com/problems/escape-the-ghosts/submissions/1224097962/


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dists = [abs(x[0]-target[0])+abs(x[1]-target[1]) for x in ghosts]
        steps = abs(target[0])+abs(target[1])
        return all(d > steps for d in dists)
