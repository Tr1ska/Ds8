import logging

logging.basicConfig(filename='timing.log', level=logging.INFO)

import time

def timing(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time
    print(result)
    logging.info(f"Функція '{func.__name__}' виконана за {execution_time} секунд")
def example_function():
    time.sleep(2)
result, execution_time = timing(example_function)
print(f"Результат: {result}")
print(f"Час виконання: {execution_time} секунд")
