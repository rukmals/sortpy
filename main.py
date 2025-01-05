# import matplotlib
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# matplotlib.use("TkAgg")  # Or "Qt5Agg"
from sortpython.visualize.SortVisualizer import SortVisualizer
# from algorithms.BubbleSort import BubbleSort
# from algorithms.CountingSort import CountingSort
from sortpython.algorithms.TimSort import TimSort
# from algorithms.MergeSort import MergeSort
# from algorithms.InsertionSort import InsertionSort

if __name__ == "__main__":
    # Input data
    # data = [4, 2, 2, 8, 3, 3, 1]

    # Using sort method


    # Array to be sorted
    data = [64, 34, 25, 12, 22, 11, 90]

    # Call the sort method
    # sorted_array = MergeSort.sort(data)
    # #
    # # # Print the sorted array
    # print("Sorted Array:", data)

    # Ask the user if they want to visualize the sorting
    visualize = True#input("Do you want to visualize the sorting process? (y/n): ").strip().lower() == 'y'
    #
    if visualize:
        visualizer = SortVisualizer(data, 500)
        steps_generator = TimSort.sort_with_visualization(data)
        visualizer.capture_steps(steps_generator)
        visualizer.animate()
        print("Sorted Array:", data)
    else:
        TimSort.sort(data)
        print("Sorted Array:", data)
    # Example without visualization:
