
import pandas as pd
from textblob import TextBlob

column = [1, 2]
attempt1 = str(pd.read_excel('Datasets\Dell Output PROCESSED.xlsx', usecols = column, ))
print(attempt1)

blob = TextBlob(attempt1)
unigrams = blob.ngrams(n=1)
bigrams = blob.ngrams(n=2)
trigrams = blob.ngrams(n=3)
count = 1
for i in range(len(unigrams)):
    for j in range(i + 1, len(unigrams)):
        if(unigrams[i] == unigrams[j]):
            count += 1
    if (count > 1):
        print (unigrams[i])
        print (count)
    count = 1

for i in range(len(bigrams)):
    for j in range(i + 1, len(bigrams)):
        if(bigrams[i] == bigrams[j]):
            count += 1
    if (count > 1):
        print (bigrams[i])
        print (count)
    count = 1

for i in range(len(trigrams)):
    for j in range(i + 1, len(trigrams)):
        if(trigrams[i] == trigrams[j]):
            count += 1
    if (count > 1):
        print (trigrams[i])
        print (count)
    count = 1

