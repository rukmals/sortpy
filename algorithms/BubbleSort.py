class BubbleSort:
    """
    A class to perform Bubble Sort with optional visualization.
    """

    @staticmethod
    def sort(arr):
        """
        Perform Bubble Sort on an array.

        :param arr: List of integers to be sorted.
        :return: The sorted array.
        """
        n = len(arr)
        for i in range(n):
            # Last i elements are already sorted
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    # Swap if the element found is greater than the next element
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def sort_with_visualization(arr):
        """
        Perform Bubble Sort on an array with visualization.

        :param arr: List of integers to be sorted.
        :return: A generator yielding intermediate states of the array.
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                yield arr.copy()  # Yield current state before comparing
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    yield arr.copy()  # Yield state after swapping
        yield arr.copy()  # Final sorted state
