# -*- coding: utf-8 -*-

#    File Name：       1.12 序列中出现次数最多的元素
#    Description :
#    Author :          LvYang
#    date：            2019/8/20
#    Change Activity:  2019/8/20:



words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)


print(word_counts['eyes'])


morewords = ['why','are','you','not','looking','in','my','eyes']

for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])



# >>> a = Counter(words)
# >>> b = Counter(morewords)
# >>> a
# Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2,
# "you're": 1, "don't": 1, 'under': 1, 'not': 1})
# >>> b
# Counter({'eyes': 1, 'looking': 1, 'are': 1, 'in': 1, 'not': 1, 'you': 1,
# 'my': 1, 'why': 1})
# >>> # Combine counts
# >>> c = a + b
# >>> c
# Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2,
# 'around': 2, "you're": 1, "don't": 1, 'in': 1, 'why': 1,
# 'looking': 1, 'are': 1, 'under': 1, 'you': 1})
# >>> # Subtract counts
# >>> d = a - b
# >>> d
# Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2,
# "you're": 1, "don't": 1, 'under': 1})
# >>>