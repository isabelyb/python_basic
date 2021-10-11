
def remove_duplicates(some_list):
    set_without_duplicates = set(some_list)
    list_without_duplicates = list(set_without_duplicates)
    return list_without_duplicates
 

def run():
    random_list = [1,1,2,2,4]
    print(remove_duplicates(random_list))


if __name__ == '__main__':
    run()