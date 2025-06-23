import nltk
nltk.download('punkt_tab')
from nltk import word_tokenize
from nltk.util import ngrams

sample_text = 'Hello! My name is Yahia, but you may know me as "The Cavalry".'
tokens = word_tokenize(sample_text)

# Unigram
unigrams = list(ngrams(tokens, 1))
print('Unigrams:', unigrams)

# Bigram
bigrams = list(ngrams(tokens, 2))
print('Bigrams:', bigrams)

# Trigram
trigrams = list(ngrams(tokens, 3))
print('Trigrams:', trigrams)