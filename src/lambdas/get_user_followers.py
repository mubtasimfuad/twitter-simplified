import json
from services import FollowService


def lambda_handler(event, context):
    user_id = event["queryStringParameters"]["user_id"]

    # Create a FollowService and get user's followers
    follow_service = FollowService()
    user_followers = follow_service.get_user_followers(user_id)

    return {"statusCode": 200, "body": json.dumps(user_followers)}
