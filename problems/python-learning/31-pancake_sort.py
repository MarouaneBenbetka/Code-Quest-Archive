class Solution:

    def pancakeSort(self, arr):
        def _filp_iteration(arr, i):
            start = 0
            end = i

            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(arr)
        res = []
        for i in range(n-1, -1, -1):
            max_index = i
            for j in range(i, -1, -1):
                if arr[j] > arr[max_index]:
                    max_index = j

            if max_index == i:
                continue
            _filp_iteration(arr, max_index)
            _filp_iteration(arr, i)

            res.append(max_index+1)
            res.append(i+1)
        return res
