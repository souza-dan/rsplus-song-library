import time
from random import uniform


def random_sleep(min_seconds: float = 1, max_seconds: float = 10) -> None:
    """
    Waits for a random amount of time between min and max range in seconds.
    """
    random_wait_time = uniform(min_seconds, max_seconds)
    time.sleep(random_wait_time)
