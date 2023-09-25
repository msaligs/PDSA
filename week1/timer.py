import time
class TimerError(Exception):
    '''
        A custom exception used to report error of timer class
    '''

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = None

    def start(self):
        if self.start_time is not None:
            raise TimerError("Timer is running. Use .stop() to stop the timer")
        self.start_time = time.perf_counter()
    def stop(self):
        if self.start_time == None:
            raise TimerError("Timer is not running. Use .start() to stop the timer.")
        self.elapsed_time = time.perf_counter() - self.start_time
        self.start_time = None
    def elapsed(self):
        '''
            Report elapsed time
        '''
        if self.elapsed_time is None:
            raise TimerError("Timer has not been run yet. Use .start() to run the timer.")
        return self.elapsed_time 
    
    def __str__(self):
        ''' prints elapsed time'''
        return str(self.elapsed_time)
    