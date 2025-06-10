from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
def analyze_sentiment_textblob(text):
  sentiment = TextBlob(text).sentiment.polarity
  if sentiment >0:
    return "Positive"
  elif sentiment <0:
     return "Negative"
  else:
    return "Neutral"
def analyze_sentiment_vader(text):
  analyzer = SentimentIntensityAnalyzer()
  sentiment = analyzer.polarity_scores(text)['compound']
  if sentiment >0.05:
    return "Positive"
  elif sentiment <-0.05:
      return "Negative"
  else:
    return "Neutral"
def analyze_input():
    text = input("Enter a sentence: ")
    print(f"Text Blib Sentiment:{analyze_sentiment_textblob(text)}")
    print(f"Vader Sentiment:{analyze_sentiment_vader(text)}")
analyze_input()
