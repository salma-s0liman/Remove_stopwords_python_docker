import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('punkt')
nltk.download('stopwords')
print(stopwords.fileids())
stoplist=stopwords.words('english')
print(stoplist)

#read the text File
with open("random_paragraphs.txt","r") as file:
  text = file.read()


#Remove stop words from text
word_tokens = word_tokenize(text)
filtered_text = [w for w in word_tokens if  w.lower() not in stoplist]
print( " ".join(filtered_text))

#Count Frequency of each word
counts = Counter(filtered_text)
print(counts)

#Disply the remaining words and their counts side by side
for word, count in counts.items():
  print(f"{word}:{count}")

