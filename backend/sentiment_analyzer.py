import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

from nltk.sentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:

    def __init__(self):
        nltk.download('vader_lexicon')
        self.sid = SentimentIntensityAnalyzer()

    def get_sentiment(self, comment):
        """
        gets sentimental value (positive, negative, or neutral) of a comment
        returns a string representation of the value
        """

        # clean comment
        comment = comment.replace('\n', ' ')
        new = ""
        for ch in comment:
            if ch.isalnum() or ch.isspace():
                new += ch
        comment = new

        # get sentimental polarity
        scores = self.sid.polarity_scores(comment)
        sentiment_polarity = scores['compound']

        # classify comment
        if sentiment_polarity > 0:
            sentiment = "positive"
        elif sentiment_polarity < 0:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        return sentiment

