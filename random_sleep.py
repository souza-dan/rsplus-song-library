import time
from random import uniform


def random_sleep():
    """
    Waits for a random amount of time between 1 and 2 seconds.
    """
    random_wait_time = uniform(1, 10)
    time.sleep(random_wait_time)

