from abc import ABC
from shared.Sort import Sort


class TimSort(Sort, ABC):
    MIN_RUN = 32  # Move this to class-level since it doesn't rely on `self`.

    @staticmethod
    def sort(arr):
        n = len(arr)

        # Step 1: Sort small runs using Insertion Sort
        for start in range(0, n, TimSort.MIN_RUN):
            end = min(start + TimSort.MIN_RUN - 1, n - 1)
            TimSort.insertion_sort(arr, start, end)

        # Step 2: Merge runs using Merge Sort logic
        size = TimSort.MIN_RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min(n - 1, left + 2 * size - 1)

                if mid < right:
                    TimSort.merge(arr, left, mid, right)
            size *= 2

    @staticmethod
    def sort_with_visualization(input_array):
        pass  # Implement visualization logic if needed.

    @staticmethod
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    @staticmethod
    def merge(arr, left, mid, right):
        # Create temporary arrays
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]

        # Merge the temporary arrays back into arr
        i = 0
        j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
