import json
from services import TweetService


def lambda_handler(event, context):
    user_id = event["queryStringParameters"]["user_id"]
    tag = event["queryStringParameters"]["tag"]

    # Create a TweetService and get tweets with a certain tag
    tweet_service = TweetService()
    tagged_tweets = tweet_service.get_tweets_with_tag(user_id, tag)

    return {"statusCode": 200, "body": json.dumps(tagged_tweets)}
