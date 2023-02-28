# encoding: utf-8
import statistics    # Common practice to do all imports at the start of a program

class DataStore:
    """
    Store of measurements and times
    """

    def __init__(self):    # The init method is run when the program is run
        self.times = []
        self.measurements = []

    def add_measurement(self, date, value):
        """
        Add the given value to the data store

        :param date: Date of the measurement
        :type date: str

        :param value: Value to add
        :type value: int or float
        """

        self.measurements.append(value)
        self.times.append(date)

    def print_measurements(self):
        """
        print the measurements and times
        """

        for time, value in zip(self.times, self.measurements):
            print(time, value)

    def get_max(self):
        """
        Returns the maximum measurment value and the time of that measurement.
        """
        # Within the class 'self' is the object and 'measurements' is an attribute of that object
        # Add_measurement and print_measurement, and get_max are methods that can be applied to the object
        # Outside of the class, the object created as an intstance of the class is what is worked upon e.g.
        # store = DataStore    # Created an instance of DataStore, so 'store' is the object outside whereas 'self' is the object inside
        # store.measurements
        max_meas = max(self.measurements)
        max_time = self.times[self.measurements.index(max_meas)]
        return [max_time, max_meas]

    def get_min(self):
        """
        Returns the minimum measurment value and the time of that measurement.
        """    
        min_meas = min(self.measurements)
        min_time = self.times[self.measurements.index(min_meas)]
        return [min_time, min_meas]

    def get_mean(self):
        """
        Returns the mean measurement value.
        """
        mean_meas = statistics.mean(self.measurements)
        return mean_meas
        
