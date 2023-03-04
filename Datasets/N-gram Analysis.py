
import pandas as pd


#data = pd.Series([1,2,3])
#print(data)
column = [1, 1]
head = 0
attempt1 = str(pd.read_excel('Datasets\Dell Output PROCESSED.xlsx', usecols = column, header = head))
print("attempt equals" + attempt1)

from textblob import TextBlob
blob = TextBlob(attempt1)
unigrams = blob.ngrams(n=1)
bigrams = blob.ngrams(n=2)
trigrams = blob.ngrams(n=3)

print(trigrams)
