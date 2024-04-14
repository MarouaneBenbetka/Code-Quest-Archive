# https://www.geeksforgeeks.org/problems/selection-sort/1

class Solution:
    def select(self, arr, i, n):
        min_value = float('inf')
        min_index = -1
        for j in range(i, n):
            if arr[j] < min_value:
                min_value = arr[j]
                min_index = j

        return min_index

    def selectionSort(self, arr, n):

        for i in range(n-1):
            minimum = self.select(arr, i, n)
            arr[i], arr[minimum] = arr[minimum], arr[i]

        return arr
