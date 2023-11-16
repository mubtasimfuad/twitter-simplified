import json
from models import Tweet
from services import TweetService


def lambda_handler(event, context):
    tweet_data = json.loads(event["body"])
    tweet = Tweet(**tweet_data)

    # Create a TweetService and post the tweet
    tweet_service = TweetService()
    tweet_service.post_tweet(tweet)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Tweet posted successfully"}),
    }
