from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from textblob import TextBlob

reviews = ['This movie was fantastic! A must-watch.',
    'I hated this movie very much.',
    'Amazing storyline and great acting!',
    'The plot was boring.',
    'Loved the cinematography! Highly recommended.']

labels = ['positive', 'negative', 'positive', 'negative', 'positive']
corrected_reviews = [str(TextBlob(review).correct()) for review in reviews]


vectorizer = CountVectorizer()
x = vectorizer.fit_transform(corrected_reviews)

x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print('Accuracy:', accuracy)

if accuracy > 0.8:
  print('Good vibes. Book the ticket!')
else:
  print('Needs more work!')