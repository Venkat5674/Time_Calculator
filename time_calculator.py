def add_time(start, duration, starting_day=None):
    # Days of the week for reference
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Split the start time into components
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Convert start time to 24-hour format
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0

    # Split the duration into components
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate the new time
    end_hour = start_hour + duration_hour
    end_minute = start_minute + duration_minute

    # Handle minute overflow
    if end_minute >= 60:
        end_hour += end_minute // 60
        end_minute %= 60

    # Calculate the number of days that have passed
    days_later = end_hour // 24
    end_hour %= 24

    # Convert back to 12-hour format
    if end_hour == 0:
        final_hour = 12
        final_period = 'AM'
    elif end_hour < 12:
        final_hour = end_hour
        final_period = 'AM'
    elif end_hour == 12:
        final_hour = 12
        final_period = 'PM'
    else:
        final_hour = end_hour - 12
        final_period = 'PM'

    # Format the minutes
    final_minute = f'{end_minute:02}'

    # Determine the final day of the week
    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        final_day_index = (starting_day_index + days_later) % 7
        final_day = days_of_week[final_day_index]
    else:
        final_day = None

    # Construct the result string
    result = f'{final_hour}:{final_minute} {final_period}'
    if final_day:
        result += f', {final_day}'
    if days_later == 1:
        result += ' (next day)'
    elif days_later > 1:
        result += f' ({days_later} days later)'

    return result

# Example test cases
print(add_time('3:30 PM', '2:12'))  # '5:42 PM'
print(add_time('11:55 AM', '3:12'))  # '3:07 PM'
print(add_time('2:59 AM', '24:00'))  # '2:59 AM (next day)'
print(add_time('11:59 PM', '24:05'))  # '12:04 AM (2 days later)'
print(add_time('8:16 PM', '466:02'))  # '6:18 AM (20 days later)'
print(add_time('3:30 PM', '2:12', 'Monday'))  # '5:42 PM, Monday'
print(add_time('2:59 AM', '24:00', 'saturDay'))  # '2:59 AM, Sunday (next day)'
print(add_time('11:59 PM', '24:05', 'Wednesday'))  # '12:04 AM, Friday (2 days later)'
print(add_time('8:16 PM', '466:02', 'tuesday'))  # '6:18 AM, Monday (20 days later)'
