# from time import sleep

# def fibonacci_gen():
#     a, b = 0, 1
#     max_num = 1600
#     contador = a
#     while max_num > contador:
#         yield a
#         a, b = b, a+b
#         contador = a


# if __name__ == "__main__":
#     fibonacci = fibonacci_gen()
#     for element in fibonacci:
#         print(element)
#         sleep(0.1)

import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

if __name__ == '__main__':
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(.05)