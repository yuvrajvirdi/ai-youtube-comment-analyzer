# ai-youtube-comment-analyzer

YouTube comment analyzer for comment sentiment analysis, spam detection, topic modeling, and classification
Each comment is analyzed in the following format:

`comment`: the comment text  <br />
`isSpam`: boolean value on if the comment is spam using a Multinomial Naive Bayes model
`author`: name of the comment author
`likeCount`: numerical like count
`publishedDate`: published date
`sentiment`: the sentiment of a comment, which is positive if the sentimental polarity is above 0, negative if below 0, and neutral if it is 0. This is done using NLTK
`topic`: a list of topics from the comment made using NLTK methods such as tokenization and LDA modelling
`type`: the classification of the comment, which can either be a question, statement, feedback, or remark. Used hard-coded synthetic training data and once again used tokenization along with a Word Net Lemmatizer

# Setup

Clone the git repository
```bash
git clone https://github.com/yuvrajvirdi/ai-youtube-comment-analyzer.git
```

## Frontend

head into the frontend folder, and install all of the dependencies

```bash
cd frontend && npm install
```

then run the application

```bash
npm run dev
```

## Backend

I included a bash script to streamline backend setup. Run this script to execute it.

```bash
chmod +x run_backend.sh
```

```bash
./run_backend.sh
```

# How it works

1. Enter your youtube video URL into the search box
2. Analyze results

## Video Demo

https://github.com/yuvrajvirdi/ai-youtube-comment-analyzer/assets/81879713/fc061069-4c31-4c42-8ef0-1e3d094f04d5





