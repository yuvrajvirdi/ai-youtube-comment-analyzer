import json
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
api_key = 'secret'

class Comments:

    def __init__(self, video_id, max_results):
        self.video_id = video_id
        self.max_results = max_results

    def get_video_comments(self):
        """ 
        fetches comment infomration from Youtube (Google Cloud) API in a list format 
        returns list of comments where each elem is a dictionary of info for the comment
        """

        # fetch comments from Youtube Data API, using Google Cloud
        url = "https://www.googleapis.com/youtube/v3/commentThreads?key="+api_key+"&textFormat=plainText&part=snippet&videoId="+self.video_id+"&maxResults="+self.max_results
        res = urllib.request.urlopen(url)

        # load as json
        data = json.loads(res.read().decode())

        comments = []

        # iterates through items in json
        for item in data['items']:
            # access comment info
            cur_item = item['snippet']['topLevelComment']['snippet']
            text = cur_item['textOriginal']
            author = cur_item['authorDisplayName']
            author_profile_picture_url = cur_item['authorProfileImageUrl']
            author_channel_url = cur_item['authorChannelUrl']
            like_count = cur_item['likeCount']
            publish_date = cur_item['publishedAt']
            comment = {
                "text": text,
                "author": author,
                "authorProfilePictureUrl": author_profile_picture_url,
                "authorChannelUrl": author_channel_url,
                "likeCount": like_count,
                "publishedDate": publish_date
            }

            # add comment info dict to comment list
            comments.append(comment)

        return comments
