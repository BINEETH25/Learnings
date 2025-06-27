# Monotonic Stack
class DailyTemperatureSolver:
    def __init__(self, temperatures):
        # Initialize with the input temperature list
        self.temperatures = temperatures

    def solve(self):
        n = len(self.temperatures)
        answer = [0] * n  # Result array initialized to 0s
        stack = []  # Monotonic decreasing stack (stores indices)

        for i in range(n):
            current_temp = self.temperatures[i]

            # While stack is not empty and current temp is warmer than stack top
            while stack and current_temp > self.temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index  # Days until warmer temperature

            # Push current index to stack (waiting for a warmer day)
            stack.append(i)

        return answer
temps = [73, 74, 75, 71, 69, 72, 76, 73]
solver = DailyTemperatureSolver(temps)
print(solver.solve())  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
