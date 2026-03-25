import threading
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()
        # print(f"{func.__name__} took {end - start:.6f} seconds")
        print(f"{func} took {end - start:.6f} seconds")  # if use @wraps from functools

        return result

    return wrapper


def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(2)  # Simulate some work (add delays for 2 sec )
    print(f"Thread {num}: Finishing")


@timer
def multithreading():
    threads = []
    for i in range(3):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()  # Wait for all threads to finish
    print("All threads completed.")


multithreading()
