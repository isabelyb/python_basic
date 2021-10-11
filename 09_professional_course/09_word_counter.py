from collections import Counter

# word = "mississippi"
# counter = {}

# for letter in word:
#      if letter not in counter:
#          counter[letter] = 0
#      counter[letter] += 1


# sales = Counter(banana=15, tomato=4, apple=39, orange=30)
# sales.most_common(1)


# data_set = "Welcome to the world of Geeks " \
# "This portal has been created to provide well written well" \
# "thought and well explained solutions for selected questions " \
# "If you like Geeks for Geeks and would like to contribute " \
# "here is your chance You can write article and mail your article " \
# " to contribute at geeksforgeeks org See your article appearing on " \
# "the Geeks for Geeks main page and help thousands of other Geeks" \
  
# # split() returns list of all the words in the string
# split_it = data_set.split()
# #print(split_it)


# #Remove some stopwords
# stopwords = ['to', 'and', 'for', 'the', 'of']
# split_it_without_stopwords = [word for word in split_it if word not in stopwords]
# #print(split_it_without_stopwords)


# # Pass the split_it list to instance of Counter class.
# Counter = Counter(split_it_without_stopwords)
# print(Counter)

# # most_common() produces k frequently encountered
# # input values and their respective counts.
# most_occur = Counter.most_common(4)  
# print(most_occur)

# for w in Counter.most_common(6):
#     print(f"{w[0]}: {w[1]}")


#########################################################################


# file = open("/home/isa/estudio/Python/python_basic/09_professional_course/08_chilanga_banda_lyrics.txt", "rt")

# data = file.read()

# total_words = data.split()

# stopwords = ['y','Y','la','de','una','los', 'me', 'No', 'con', 'que']

# words = [word for word in total_words if word not in stopwords]

# words_number = len(words)

# wordcount = Counter(words)

# for w in wordcount.most_common(10):
#     print(f"{w[0]}: {w[1]}")


##########################################

# def word_counter(func):
#     def counter(*args, **kwargs):
#         data = func(*args, **kwargs)    
#         total_words = data.split()
#         stopwords = ['y','Y','la','de','una','los', 'me', 'No', 'con', 'que']
#         words = [word for word in total_words if word not in stopwords]
#         wordcount = Counter(words)
#         for w in wordcount.most_common(6):
#             print(f"{w[0]}: {w[1]}")
#     return counter

# @word_counter
# def text_reader():  
#     file = open("/home/isa/estudio/Python/python_basic/09_professional_course/08_chilanga_banda_lyrics.txt", "rt")
#     data = file.read()
#     return data

# @word_counter
# def text_reader(url):  
#     file = open(url, "rt")
#     data = file.read()
#     return data

# url = "/home/isa/estudio/Python/python_basic/09_professional_course/word_counter/chilanga_banda_lyrics.txt"
# url3 = "/home/isa/estudio/Python/python_basic/09_professional_course/08_chilanga_banda_lyrics.txt"


#text_reader(url)


#######################

import urllib.request

url = urllib.request.urlopen('https://raw.githubusercontent.com/isabelyb/word_counter/main/chilanga_banda_lyrics.txt')

for line in url:
	decoded_line = line.decode("utf-8")
	print(decoded_line)



print(url)