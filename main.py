# import matplotlib
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# matplotlib.use("TkAgg")  # Or "Qt5Agg"
from visualize.SortVisualizer import SortVisualizer
from algorithms.BubbleSort import BubbleSort
from algorithms.CountingSort import CountingSort

if __name__ == "__main__":
    # Input data
    data = [4, 2, 2, 8, 3, 3, 1]

    # Using sort method
    # sorted_array = CountingSort.sort(input_array)
    # print("Sorted Array:", sorted_array)

    # Ask the user if they want to visualize the sorting
    visualize = input("Do you want to visualize the sorting process? (y/n): ").strip().lower() == 'y'

    if visualize:
        visualizer = SortVisualizer(data, 300)
        steps_generator = CountingSort.sort_with_visualization(data)
        visualizer.capture_steps(steps_generator)
        visualizer.animate()
        print("Sorted Array:", data)
    else:
        data = CountingSort.sort(data)
        print("Sorted Array:", data)
    # Example without visualization:
