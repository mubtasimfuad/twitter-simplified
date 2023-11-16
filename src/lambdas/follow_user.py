import json
from models import Follow
from services import FollowService


def lambda_handler(event, context):
    follow_data = json.loads(event["body"])
    follow = Follow(**follow_data)

    # Create a FollowService and make the user follow another user
    follow_service = FollowService()
    follow_service.follow_user(follow)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "User followed successfully"}),
    }
