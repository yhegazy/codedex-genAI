import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

sample_text = 'Hello! My name is Yahia, but you may know me as "The Cavalry".'
tokens = word_tokenize(sample_text)

print('Tokens:', tokens)