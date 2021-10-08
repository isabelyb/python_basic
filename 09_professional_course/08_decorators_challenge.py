from collections import Counter


# def word_counter(func):
#     def counter(*args, **kwargs):
#         pass
#     return counter


def text_reader():
    file = open("/home/isa/estudio/Python/python_basic/09_professional_course/08_chilanga_banda_lyrics.txt", "r", encoding="utf-8")
    wordcount = Counter(file.read().split())
    for item in wordcount.items(): print(f'{item}')



file = open("/home/isa/estudio/Python/python_basic/09_professional_course/08_chilanga_banda_lyrics.txt", "rt")
data = file.read()
words = data.split()
print(len(words))
wordcount = Counter(file.read().split())


#most_occur = words.most_common(2)
  
#print(most_occur)