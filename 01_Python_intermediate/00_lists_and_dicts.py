def run():
    my_list = [1,"Hello", True, 4.5]
    my_dict = {"firstname": "Isabel", "lastname": "Yepes"}

    super_list = [
        {"firstname": "Isabel", "lastname": "Yepes"},
        {"firstname": "Mario", "lastname": "Melo"},
        {"firstname": "Pepito", "lastname": "Perez"},
        {"firstname": "Juana", "La Loca": "Yepes"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key,"", value)
        
    for dictionaries in super_list:
        print (dictionaries)

    for dictionaries in super_list:
        for key, value in dictionaries.items():
            print(f'{key}: {value}')

if __name__ == '__main__':
    run()

