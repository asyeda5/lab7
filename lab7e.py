#!/usr/bin/env python3
# Student ID: [seneca_id]

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, __str__, __repr__,
                            time_to_sec, format_time,
                            change_time, sum_times
    """
    
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        '''Return a string representation for the object self'''
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
    
    def __repr__(self):
        '''Return a string representation for the object self'''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'
    
    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
    
    def sum_times(self, t2):
        """Add two time objects and return the sum."""
        # Convert both times to seconds
        t1_seconds = self.time_to_sec()
        t2_seconds = t2.time_to_sec()
        
        # Sum the times in seconds
        total_seconds = t1_seconds + t2_seconds
        
        # Convert the total seconds back to a time object
        return sec_to_time(total_seconds)
    
    def change_time(self, seconds):
        """Change time by adding or subtracting seconds"""
        time_sec

