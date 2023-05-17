import gensim
from gensim import corpora
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class TopicModeller():

    def __init__(self, num_topics=4, num_words=5):
        self.num_topics = num_topics
        self.num_words = num_words
        self.stop_words = set(stopwords.words('english'))

    def preprocess(self, comment):
        """ 
        tokenize comment + remove stop words
        return tokens
        """
        tokens = []
        for word in word_tokenize(comment):
            if word.lower() not in self.stop_words and word.isalnum():
                tokens.append(word.lower())

        return tokens

    def get_topic(self, comment):
        """ 
        gets topic of comment input 
        returns top topics of comment
        """

        # if comment is empty, somehow
        if not comment: return []

        # preprocess comment
        tokens = self.preprocess(comment)

        # check if tokens are empty
        if not tokens: return []

        # create dictionary and corpus
        dictionary = corpora.Dictionary([tokens])
        corpus = [dictionary.doc2bow(tokens)]

        # perform LDA modeling
        lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=self.num_topics)

        # get topics for the comment
        topics = []
        for topic_id, prob in lda_model.get_document_topics(corpus[0], minimum_probability=0.1):
            top_words = [word for word, _ in lda_model.show_topic(topic_id, topn=self.num_words)]
            topics.append(', '.join(top_words))

        return list(set(topics))