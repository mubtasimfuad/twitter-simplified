import json
from services import TweetService


def lambda_handler(event, context):
    user_id = event["queryStringParameters"]["user_id"]

    # Create a TweetService and get tweets from user's followers
    tweet_service = TweetService()
    followers_tweets = tweet_service.get_followers_tweets(user_id)

    return {"statusCode": 200, "body": json.dumps(followers_tweets)}
