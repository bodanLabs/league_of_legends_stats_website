from datetime import datetime, timedelta

def get_time_difference(timestamp):

    # New timestamp from API
    new_api_timestamp = timestamp / 1000  # Convert milliseconds to seconds

    # Current timestamp
    current_timestamp = datetime.now().timestamp()

    # Calculate the new difference in seconds
    new_time_difference_seconds = current_timestamp - new_api_timestamp

    # Convert the new difference to timedelta for easier manipulation
    new_time_difference = timedelta(seconds=new_time_difference_seconds)

    # Convert to days, hours, and minutes for the new timestamp
    new_days = new_time_difference.days
    new_hours, new_remainder = divmod(new_time_difference.seconds, 3600)
    new_minutes, new_seconds = divmod(new_remainder, 60)

    # Format the new output
    if new_days > 0:
        new_time_difference_str = f"{new_days} days, {new_hours} hours, and {new_minutes} minutes"
    elif new_hours > 0:
        new_time_difference_str = f"{new_hours} hours and {new_minutes} minutes"
    else:
        new_time_difference_str = f"{new_minutes} minutes"

    return new_time_difference_str