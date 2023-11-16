# Simplified Twitter Backend

## Summary

This project is a serverless AWS SAM (Serverless Application Model) application that serves as the backend for a simplified version of Twitter. The backend includes functionalities for users to post tweets, fetch their tweets, follow or unfollow other users, fetch tweets from followers, add tags to tweets, and find tweets with specific tags.

## Project Structure

```plaintext
├── events
│   └── event.json
├── __init__.py
├── README.md
├── requirements.txt
├── samconfig.toml
├── src
│   ├── __init__.py
│   ├── lambdas
│   │   ├── create_tweet.py
│   │   ├── follow_user.py
│   │   ├── get_followers_tweets.py
│   │   ├── get_tweets_with_tag.py
│   │   ├── get_user_followers.py
│   │   ├── get_user_tweets.py
│   │   ├── __init__.py
│   │   └── unfollow_user.py
│   ├── models.py
│   ├── repositories.py
│   ├── requirements.txt
│   └── services.py
├── template.yaml
└── tests
    ├── __init__.py
    ├── integration
    │   ├── __init__.py
    │   └── test_api_gateway.py
    ├── test_services.py
    └── unit
        ├── __init__.py
        └── test_handler.py
```

## AWS SAM Template

### Parameters

- **StageName**: The stage name for the deployment (default: "dev").

### Resources

- **DefaultApi**: API Gateway for Twitter features.
- **CreateTweetFunction**: Lambda function for creating a tweet.
- **GetUserTweetsFunction**: Lambda function for getting user's tweets.
- **GetFollowersTweetsFunction**: Lambda function for getting tweets from user's followers.
- **GetTweetsWithTagFunction**: Lambda function for getting tweets with a certain tag.
- **FollowUserFunction**: Lambda function for following a user.
- **UnfollowUserFunction**: Lambda function for unfollowing a user.
- **GetUserFollowersFunction**: Lambda function for getting user's followers.

### Outputs

- **DefaultApi**: API Gateway endpoint for Twitter features.

## Repository

### TweetRepository

Handles the storage and retrieval of tweets.

- `save_tweet(tweet: Tweet)`: Save a tweet.
- `get_user_tweets(user_id: str) -> List[Tweet]`: Retrieve user's tweets.
- `get_followers_tweets(user_id: str) -> List[Tweet]`: Retrieve tweets from user's followers.
- `get_tweets_with_tag(user_id: str, tag: str) -> List[Tweet]`: Retrieve tweets with a certain tag.

### FollowRepository

Handles the storage and retrieval of follow relationships.

- `follow_user(follow: Follow)`: Record a user following another user.
- `unfollow_user(follow: Follow)`: Remove a user following another user.
- `get_user_followers(user_id: str) -> List[str]`: Retrieve user's followers.

## Getting Started

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Deploy the application using AWS SAM: `sam deploy --guided`.

## Usage

Follow the API Gateway endpoint provided in the Outputs section to interact with the Twitter features.

## Contributors

- Mubtasim Fuad, Shadhin Lab LLC

## License

This project is licensed under the [MIT License](LICENSE).