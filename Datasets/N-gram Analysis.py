
import pandas as pd


#data = pd.Series([1,2,3])
#print(data)
column = [1, 1]
head = 2501
attempt1 = pd.read_excel('Datasets\Dell Output PROCESSED.xlsx', usecols = column, header = head)
print(attempt1)

from textblob import TextBlob
blob = TextBlob(attempt1)
