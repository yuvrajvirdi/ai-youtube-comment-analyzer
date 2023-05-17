import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import joblib


class SpamDetector:

    def __init__(self):
        # load dataframe
        df = pd.read_csv("data/Youtube01-Psy.csv")
        df_data = df[['CONTENT', 'CLASS']]

        # features and labels
        df_x = df_data['CONTENT']
        df_y = df_data.CLASS

        # use CountVectorizer to extract features
        self.cv = CountVectorizer()
        corpus = df_x
        X = self.cv.fit_transform(corpus)
        X_train, X_test, y_train, y_test = train_test_split(X, df_y, test_size=33, random_state=42)

        # Naive Bayes
        self.clf = MultinomialNB()
        self.clf.fit(X_train, y_train)
        self.clf.score(X_test, y_test)

        # serialize model
        joblib.dump(self.clf, 'model.pkl')

        self.clf = joblib.load('model.pkl')

    def get_prediction(self, comment):
        """
        makes a prediction on the inputted comment
        """
        if not comment: return False

        data = [comment]
        vector = self.cv.transform(data).toarray()
        prediction = self.clf.predict(vector)

        # if 1, then it's spam, otherwise it's not
        is_spam = True if prediction[0] == 1 else False

        return is_spam