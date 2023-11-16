import json
from services import TweetService


def lambda_handler(event, context):
    user_id = event["queryStringParameters"]["user_id"]

    # Create a TweetService and get user's tweets
    tweet_service = TweetService()
    user_tweets = tweet_service.get_user_tweets(user_id)

    return {"statusCode": 200, "body": json.dumps(user_tweets)}
