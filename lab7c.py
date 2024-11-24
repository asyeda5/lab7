class Time:
    def __init__(self, hour=0, minute=0, second=0):
        """Initialize the Time object with hour, minute, and second."""
        # Check if any of the arguments is not an integer
        if not all(isinstance(arg, int) for arg in [hour, minute, second]):
            raise TypeError("Hour, minute, and second must be integers.")
        
        # Initialize the time attributes
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return the time as a string in HH:MM:SS format."""
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):   
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, td):
    '''add a time duration td to a time t1'''
    t1_seconds = time_to_sec(t1)
    td_seconds = time_to_sec(td)
    total_seconds = t1_seconds + td_seconds
    return sec_to_time(total_seconds)

def change_time(t, seconds_change):
    '''change the time t by seconds_change (can be positive or negative)'''
    t_seconds = time_to_sec(t)
    new_seconds = t_seconds + seconds_change
    return sec_to_time(new_seconds)

def format_time(t):
    '''return the time in HH:MM:SS format'''
    return f"{t.hour:02}:{t.minute:02}:{t.second:02}"


