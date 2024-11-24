 #!/usr/bin/env python3
# Student ID: [seneca_id]

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        '''Return time as HH:MM:SS'''
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
    
    def __repr__(self):
        '''Return time as HH.MM.SS'''
        return f"{self.hour:02d}.{self.minute:02d}.{self.second:02d}"

    def sum_times(self, t2):
        '''Sum the time with another time object and return the result'''
        total_seconds = (self.hour * 3600 + self.minute * 60 + self.second) + (t2.hour * 3600 + t2.minute * 60 + t2.second)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return Time(hours, minutes, seconds)

# Test if the file exists and is being executed correctly
def test_time_object():
    # Create two time objects
    t1 = Time(1, 45, 30)
    t2 = Time(2, 15, 50)

    # Print out time objects
    print("Time 1:", t1)  # Should use __str__
    print("Time 2:", t2)  # Should use __str__

    # Sum times using sum_times method
    result = t1.sum_times(t2)
    print("Sum of Time 1 and Time 2:", result)  # Should use __str__

    # Show the string representation using __repr__
    print("String representation of Time 1:", repr(t1))
    print("String representation of Time 2:", repr(t2))

# Run the test function to check functionality
if __name__ == "__main__":
    test_time_object()


