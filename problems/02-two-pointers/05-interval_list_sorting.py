# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList == [] or secondList == []:
            return []

        p1 = p2 = 0

        result = []
        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]

            if end1 < start2:
                p1 += 1
            elif end2 < start1:
                p2 += 1
            else:
                result.append([max(start1, start2), min(end1, end2)])
                if end1 < end2:
                    p1 += 1
                else:
                    p2 += 1

        return result
