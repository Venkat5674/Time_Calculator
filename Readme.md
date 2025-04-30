# Time Calculator

## Project Overview
The Time Calculator is a Python project that calculates the time after adding a specific duration to a given start time. It also optionally displays the day of the week and handles time transitions across days.

## Features
- Adds a duration to a specified start time in 12-hour format.
- Handles day transitions accurately (e.g., next day, multiple days later).
- Optionally accepts a starting day of the week and calculates the resulting day.

## Example Usage
```python
from time_calculator import add_time

print(add_time("3:00 PM", "3:10"))  # Output: "6:10 PM"
print(add_time("11:30 AM", "2:32", "Monday"))  # Output: "2:02 PM, Monday"
print(add_time("10:10 PM", "3:30"))  # Output: "1:40 AM (next day)"
print(add_time("11:43 PM", "24:20", "Tuesday"))  # Output: "12:03 AM, Thursday (2 days later)"
```

## Features Explained
1. **Time Format**:
   - Accepts time in 12-hour format (e.g., "3:00 PM").
   - Returns the result in the same format.

2. **Day Calculation**:
   - Handles transitions to the next day or multiple days later.
   - Calculates the resulting day of the week if a starting day is provided.

3. **Validation**:
   - Ensures valid input for time and duration.

## How to Run
- Use the `add_time` function in Python to calculate the resulting time after adding a duration.
