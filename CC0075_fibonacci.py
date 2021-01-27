desired_range = 55  # Returns all Fibonacci numbers range up to desired number
fibonacci = [1, 1]  # First two numbers of the series - default values
i = 0
while max(fibonacci) <= desired_range:
    fibonacci.append(fibonacci[i]+fibonacci[i+1])
    i += 1
fibonacci.pop()  # Code goes on to add one last value to the series once the condition is satisfied,so last one removed
print(f"Fibonacci range up to {desired_range} is → {fibonacci}")