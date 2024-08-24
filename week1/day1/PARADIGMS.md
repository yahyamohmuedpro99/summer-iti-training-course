

![alt text](/summer-iti-training-course/media/paradigms.png)
### 1\. **Imperative Programming (Python)**

```python
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print(f"Total sum is: {total}")`
```
**Explanation**:

-   **How It Works**: Imperative programming focuses on **how** to perform tasks. The code explicitly tells the computer to start with a total of `0`, then loop through each number in the list, adding it to `total`. Finally, it prints the sum.
*so it all about change the state*
-   **Characteristics**: Uses loops and state changes. The `total` variable is mutable and gets updated in each iteration.

### 2\. **Object-Oriented Programming (Python)**

```python
`class NumberList:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_sum(self):
        total = 0
        for num in self.numbers:
            total += num
        return total

numbers = NumberList([1, 2, 3, 4, 5])
print(f"Total sum is: {numbers.calculate_sum()}")`
```
**Explanation**:

-   **How It Works**: OOP focuses on organizing code around objects, which are instances of classes. Here, the `NumberList` class contains both the data (`numbers`) and the method (`calculate_sum`) that operates on that data.
-   **Characteristics**: Encapsulation (data and behavior are bundled in the `NumberList` class), and methods are used to manipulate object state.

### 3\. **Functional Programming (Python)**

```python
# Functional approach to sum a list of numbers
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)

print(f"Total sum is: {total}")`
```
**Explanation**:

-   **How It Works**: Functional programming emphasizes **what** to do rather than **how** to do it. The `reduce` function takes a lambda function (which adds two numbers) and applies it across the list, accumulating the result.
-   **Characteristics**: Avoids changing states and mutable data. The `lambda` function and `reduce` are used instead of loops or mutable variables.

### 4\. **Declarative Programming (SQL)**

```sql
-- Declarative approach to sum a list of numbers
-- Assuming there's a table named 'numbers' with a column 'value'

SELECT SUM(value) AS total_sum
FROM numbers;`
```
**Explanation**:

-   **How It Works**: Declarative programming specifies **what** the outcome should be without detailing **how** to achieve it. Here, the SQL query requests the sum of the `value` column, and the database engine determines the best way to calculate it.
-   **Characteristics**: Focuses on the end result, not the process. The programmer declares the goal (summing values) rather than writing a step-by-step procedure.

## Summary

**Imperative Programming**: How to perform tasks with explicit state changes and step-by-step instructions.

**Object-Oriented Programming**: Organizes code into classes that bundle data and behavior.

**Functional Programming**: Focuses on what to do using functions and immutability, avoiding state changes.

**Declarative Programming**: Specifies what the result should be without detailing the process, leaving execution to the system.