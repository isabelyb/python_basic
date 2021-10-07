from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):  # Recibe todos los argumentos posicionales y nombrados
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper  # Porque un decorador es una nested function y debe retornarse.

@execution_time
def random_func():
    for _ in range(1,1000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return  a + b

suma(5, 5)

# random_func()

