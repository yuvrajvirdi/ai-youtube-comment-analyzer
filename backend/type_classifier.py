import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class TypeClassifier:
    
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()
        self.classifier = nltk.NaiveBayesClassifier.train(self.train_data())
    
    def train_data(self):
        """
        train data using mock data phrases
        """

        training_data = []

        # define training data for each topic
        question_data = [("how can I", "question"), ("what is the best way to", "question"), ("when should I", "question")]
        statement_data = [("you should", "statement"), ("what if you", "statement"), ("why don't you", "statement")]
        feedback_data = [("I love", "feedback"), ("I hate", "feedback"), ("this video is", "feedback")]
        remark_data = [("great video", "remark"), ("good job", "remark"), ("thanks for", "remark")]

        data = question_data + statement_data + feedback_data + remark_data
        # tokenize and preprocess training data
        for text, label in data:
            words = word_tokenize(text.lower())
            filtered_words = []
            for word in words:
                if word not in self.stop_words and word.isalnum():
                   filtered_words.append(self.lemmatizer.lemmatize(word))
            
            # Create a dictionary for the features
            features = {word: True for word in filtered_words}
            
            training_data.append((features, label))
            
        return training_data

    def get_types(self, comment):
        """
        gets the topics of the comments
        """

        # tokenize + preprocess the comment
        words = word_tokenize(comment.lower())
        filtered_words = []
        for wrd in words:
            if wrd not in self.stop_words and wrd.isalnum():
                filtered_words.append(self.lemmatizer.lemmatize(wrd))

        # classify the comment
        feature_dict = {wrd: True for wrd in filtered_words}
        prob_dist = self.classifier.prob_classify(feature_dict)
        label = prob_dist.max()
        return label
