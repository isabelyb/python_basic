def run():
    # squares = []
    # for i in range(1, 101):
    #     squares.append(i**2)
        
    # print(squares)


    # squares_a = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares_a.append(i**2)
        
    # print(squares_a)


    # squares = [i**2 for i in range(1,101) if i % 3 != 0]

    # print(squares)
    
    # numbers = [i for i in range(1,10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    # print(numbers)

    # my_dict = {i : round(i**0.5,2) for i in  range(1,1001)}

    # print(my_dict)
    
    my_dict = {}

    for i in range (1, 101):
        my_dict[i] = i**3

    print(my_dict)
    
if __name__ == '__main__':
    run()