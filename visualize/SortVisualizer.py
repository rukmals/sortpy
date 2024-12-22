import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

matplotlib.use("TkAgg")  # Or "Qt5Agg"


class SortVisualizer:
    def __init__(self, initial_data, interval):
        self.data = initial_data
        self.interval = interval
        self.steps = []  # Store states for animation
        self.fig, self.ax = plt.subplots()
        self.bar_rects = self.ax.bar(range(len(initial_data)), initial_data, color='skyblue')
        self.bar_texts = [
            self.ax.text(i, val, str(val), ha='center', va='bottom')
            for i, val in enumerate(initial_data)
        ]

    def capture_steps(self, generator):
        for state in generator:
            self.steps.append(state.copy())

    def update(self, frame):
        current_values = self.steps[frame]
        for rect, text, height in zip(self.bar_rects, self.bar_texts, current_values):
            rect.set_height(height)  # Update bar height
            text.set_position((rect.get_x() + rect.get_width() / 2, height))  # Update text position
            text.set_text(str(height))  # Update text value

    def animate(self):
        self.ax.set_title("Sorting Algorithm Visualization")
        self.ax.set_xlabel("Index")
        self.ax.set_ylabel("Value")
        self.ax.set_xticks(range(len(self.data)))

        ani = animation.FuncAnimation(
            self.fig, self.update, frames=len(self.steps), repeat=False, interval=self.interval
        )
        plt.show()
