from flask import Flask, request, jsonify
from flask_cors import CORS
from sentiment_analyzer import SentimentAnalyzer
from topic_modeller import TopicModeller
from spam_detector import SpamDetector
from type_classifier import TypeClassifier
from comments import Comments

app = Flask(__name__)
CORS(app)

spam_detector = SpamDetector()
sentiment_analyzer = SentimentAnalyzer()
topic_modeller = TopicModeller()
type_classifier = TypeClassifier()

# index route
@app.route('/')
def index():
    return """
        Youtube-Video-Assistant Backend API
    """

# comment analysis route 
@app.route('/analyze', methods=['GET'])
def analyze():
    # extract video id
    video_id = request.args.get('id')
    max_results = request.args.get('maxResults')
    
    if video_id is None:
        return "The request is missing a required parameter: id"
    else:
        # json list of comment jsons
        res = []
        # fetch comments
        comments = Comments(video_id, max_results).get_video_comments()

        # traverse comments and analyze each comment
        for comment in comments:

            comment_text = comment['text']
            author = comment['author']
            like_count = comment['likeCount']
            published_date = comment['publishedDate']
            is_spam = spam_detector.get_prediction(comment_text)

            cur = {
                "comment": comment_text,
                "isSpam": is_spam,
                "author": author,
                "likeCount": like_count,
                "publishedDate": published_date
            }

            if is_spam:
                res.append(cur)

            else:
                sentiment = sentiment_analyzer.get_sentiment(comment_text)
                topics = topic_modeller.get_topic(comment_text)
                type = type_classifier.get_types(comment_text)

                cur["sentiment"] = sentiment
                cur["topics"] = topics
                cur["type"] = type
                res.append(cur)
            
        return jsonify(res)

# comment spam prediction route
@app.route('/predict', methods=['GET'])
def predict():
    
    # extract comment from URL 
    comment = request.args.get('comment')
    if comment is None:
        return "The request is missing a required parameter: comment"
    else:
        is_spam = spam_detector.get_prediction(comment)
    
        res = {
            "comment": comment,
            "isSpan": is_spam
        }

        return jsonify(res)

# 400 error handler
@app.errorhandler(400)
def handle_400(e):
    error = 'The request is missing a required parameter: comment'
    return error

# 404 error handler
@app.errorhandler(404)
def handle_404(e):
    error = 'The requested URL was not found on the server'
    return error

# 422 error handler
@app.errorhandler(422)
def handle_422(e):
    error = 'The request contains invalid input. Please enter a valid string for the comment parameter'
    return error

# 500 error handler
@app.errorhandler(500)
def handle_500(e):
    error = 'An unknown server error has occured'
    return error

if __name__ == "__main__":
    app.run(port=5000,debug=True)
