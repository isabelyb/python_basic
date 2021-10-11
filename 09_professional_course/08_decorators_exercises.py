from collections import Counter


# def word_counter(func):
#     def counter(*args, **kwargs):
#         pass
#     return counter



def word_counter(func):
    def counter(data):        
        total_words = data.split()
        stopwords = ['y','Y','la','de','una','los', 'me', 'No', 'con', 'que']
        words = [word for word in total_words if word not in stopwords]
        wordcount = Counter(words)
        for w in wordcount.most_common(6):
            print(f"{w[0]}: {w[1]}")
        func()
    return counter

@word_counter
def text_reader():
    url = "/home/isa/estudio/Python/python_basic/09_professional_course/08_chilanga_banda_lyrics.txt"
    file = open(url, "rt")
    data = file.read()
    return data



# def text_reader():
#     file = open("/home/isa/estudio/Python/python_basic/09_professional_course/08_chilanga_banda_lyrics.txt", "r", encoding="utf-8")
#     wordcount = Counter(file.read().split())
#     for item in wordcount.items(): print(f'{item}')




# file = open("/home/isa/estudio/Python/python_basic/09_professional_course/08_chilanga_banda_lyrics.txt", "rt")
# data = file.read()
# total_words = data.split()
# stopwords = ['y','Y','la','de','una','los', 'me', 'No', 'con', 'que']
# words = [word for word in total_words if word not in stopwords]
# words_number = len(words)
# wordcount = Counter(words)
# for w in wordcount.most_common(6):
#     print(f"{w[0]}: {w[1]}")

  
def add_one(number):
    return number + 1
    
add_one(2)
## 3

def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

#####

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

####################################

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

#print(say_whee)

#say_whee()

#my_decorator(say_whee())

###################################

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

#say_whee()

