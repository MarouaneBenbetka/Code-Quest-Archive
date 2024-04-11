class Solution:

    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        for i in range(len(arr)):
            j = arr.index(n-i)
            if j != 0:
                arr = arr[:j+1][::-1] + arr[j+1:]
            arr = arr[:n-i][::-1] + arr[n-i:]
            res.extend([j+1, n-i])
        return res
